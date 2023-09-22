from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.chat_models import ChatOpenAI
import os
# from langchain.tools import BaseTool
from langchain.chains import create_tagging_chain_pydantic
from langchain.chat_models import ChatOpenAI
# import requests
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
# from datetime import datetime
# import json
load_dotenv()

from core.schemas import GetFlightInPeriodCheckInput, RequestBody
from core.constants import promptTemplate
from core.utils.bookingDetails import booking_details

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# ask_init = ["fly_from", "fly_to", "date_from", "date_to", "sort"]


llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
memory = ConversationBufferMemory(
    memory_key="chat_history")
system_template = promptTemplate
system_prompt = SystemMessagePromptTemplate.from_template(system_template)
human_template = "{input_data}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)
prompt = ChatPromptTemplate.from_messages([
    system_prompt,
    # Where the memory will be stored.
    MessagesPlaceholder(variable_name="chat_history"),
    human_prompt],
)

memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True,
    input_key="input_data",
)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

# def ask_for_info(ask_for, input_data):
#     chain_output = chain({
#         "input_data": input_data,
#         "ask_for": ask_for,
#     })
#     return chain_output

tagging_chain = create_tagging_chain_pydantic(GetFlightInPeriodCheckInput, llm)

user_flight_details = GetFlightInPeriodCheckInput(
    fly_from="", fly_to="", date_from="", date_to="", sort=""
)

def check_what_is_empty(flight_details):
    ask_for = []
    for field, value in flight_details.items():
        if value in [None, "", 0]:
            ask_for.append(f"{field}")
    return ask_for

def add_non_empty_details(current_details: GetFlightInPeriodCheckInput,new_details: GetFlightInPeriodCheckInput):
    non_empty_details = {
        k: v for k, v in new_details.dict().items() if v not in [None, "", 0]
    }
    updated_details = current_details.dict()
    updated_details.update(non_empty_details)
    return updated_details

# def filter_response(text_input, user_flight_details):
#     res = tagging_chain.run(text_input)
#     user_flight_details = add_non_empty_details(user_flight_details, res)
#     ask_for = check_what_is_empty(user_flight_details)
#     return user_flight_details, ask_for

# def get_flight_in_period(fly_from, fly_to, date_from, date_to, sort):
#     headers = {"apikey": "0tvfUPHxSK3axHyPv0wOlCKPcwcF-T7f"}
#     BASE_URL = f'https://api.tequila.kiwi.com/v2/search?fly_from={fly_from}&fly_to={fly_to}&date_from={date_from}&date_to={date_to}&sort={sort}&limit=10&curr=AUD'
#     response = requests.get(BASE_URL, headers=headers)
#     response = response.json()
#     flights = []
#     for flight in response['data']:
#         price = flight['price']
#         duration = flight['duration']['departure']/3600
#         availability = flight['availability']["seats"]
#         routes = flight['route']
#         departure= datetime.fromisoformat(flight['local_departure'][:-1])
#         arrival=datetime.fromisoformat(flight['local_arrival'][:-1])
#         details = []
#         for idx, route in enumerate(routes):
#             singleRoute={
#                 "index":idx,
#                 "route":route['airline'],
#                 "flightNo":route['flight_no'],
#                 "from":f"{route['cityFrom']}",
#                 "to":f"{route['cityTo']}"
#             }
#             details.append(singleRoute)

#         flight_info = {
#             "price": price,
#             "duration": duration,
#             "availability": availability,
#             "departure":departure.strftime("%b %d, %Y %I:%M %p"),
#             "arrival":arrival.strftime("%b %d, %Y %I:%M %p"),
#             "routes": details
#         }
#         flights.append(flight_info)
#     return flights

# def booking_details(input_data, first_msg, user_flight_details):
#     ai_response = ""
#     if first_msg:
#         ask_for = ask_init
#     user_flight_details, ask_for = filter_response(
#         input_data, user_flight_details)
#     if input_data != "yes":
#         chain_output = ask_for_info(ask_for, input_data)
#         ai_response = chain_output["text"]
#     else:
#         flights = get_flight_in_period('BLR', 'MEL', '14/09/2023','16/09/2023', 'price')
#         ai_response = "Here are the flights available for you: "
#         data=json.dumps(flights, separators=(',', ':'))
#         print(flights)
#         return {"response": ai_response, "flight_details": user_flight_details,"success":True,"data":flights}
#     return {"response": ai_response, "flight_details": user_flight_details}

app = FastAPI()

origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def handler(request: Request, body: RequestBody):
    if request.method == "POST":
        input_data = body.input
        first_msg = body.firstMsg
        if not input_data:
            raise HTTPException(status_code=400, detail="No input!")
        details = booking_details(input_data, first_msg, user_flight_details)
        return details
    else:
        raise HTTPException(status_code=405, detail="Only POST is allowed")

# To run the app:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)