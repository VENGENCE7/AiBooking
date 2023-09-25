from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_tagging_chain_pydantic
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv

from core.schemas import GetFlightInPeriodCheckInput
from core.constants import promptTemplate

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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
    memory_key="chat_history", 
    return_messages=True,
    input_key="input_data",
)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

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
