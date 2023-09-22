
import json
from core.utils.getFlights import get_flight_in_period
from core.schemas import GetFlightInPeriodCheckInput
from ai.llm import tagging_chain,chain
ask_init = ["fly_from", "fly_to", "date_from", "date_to", "sort"]

def booking_details(input_data, first_msg, user_flight_details):
    ai_response = ""
    if first_msg:
        ask_for = ask_init
    user_flight_details, ask_for = filter_response(
        input_data, user_flight_details)
    if input_data != "yes":
        chain_output = ask_for_info(ask_for, input_data)
        ai_response = chain_output["text"]
    else:
        flights = get_flight_in_period('BLR', 'MEL', '14/09/2023','16/09/2023', 'price')
        ai_response = "Here are the flights available for you: "
        data=json.dumps(flights, separators=(',', ':'))
        print(flights)
        return {"response": ai_response, "flight_details": user_flight_details,"success":True,"data":flights}
    return {"response": ai_response, "flight_details": user_flight_details}

def ask_for_info(ask_for, input_data):
    chain_output = chain({
        "input_data": input_data,
        "ask_for": ask_for,
    })
    return chain_output

def filter_response(text_input, user_flight_details):
    res = tagging_chain.run(text_input)
    user_flight_details = add_non_empty_details(user_flight_details, res)
    ask_for = check_what_is_empty(user_flight_details)
    return user_flight_details, ask_for

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