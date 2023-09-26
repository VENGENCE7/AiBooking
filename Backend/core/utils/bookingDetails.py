
import traceback,logging

from core.utils.getFlights import get_flight_in_period
# from core.schemas import GetFlightInPeriodCheckInput
from ai.llm import extraction_chain,chain
from core.constants import requiredBookingDetails

from core.utils.updateDetails import updateDetails

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def booking_details(input_data, first_msg, user_flight_details):

    try:
        ai_response = ""
        # if first_msg:
        # if input_data != "yes":
        # user_flight_details, ask_for = filter_response(input_data, user_flight_details)
        ask_for = requiredBookingDetails
        chain_output = ask_for_info(ask_for, input_data)
        dets=filter_response(chain_output['chat_history'])
        print("USER FLIGHT DETAILS ==> ",dets,type(dets))
        # so we are getting data ,just need to add check for once we have all data we can hit the api and send response to the frontend

        # ask_for=check_what_is_empty(dets)
        # print(ask_for)
        ai_response = chain_output["text"]
        # if input_data == 'yes':
        #     flights = get_flight_in_period('BLR', 'MEL', '14/10/2023','16/10/2023', 'price')
        #     ai_response = "Here are the flights available for you: "
        #     return {"response": ai_response, "flight_details": user_flight_details,"success":True,"data":flights}
        return {"response": ai_response, "flight_details": user_flight_details}
        
    except Exception as e:
        error_name = type(e).__name__
        error_message = str(e)
        traceback_str = traceback.format_exc()
        print(f"Error in booking details: {error_name} - {error_message} \n {traceback_str}")
        return {"response": f"Error: {error_name} - {error_message}"}

def ask_for_info(ask_for, input_data):
    chain_output = chain({
        "input_data": input_data,
        "requiredBookingDetails": ask_for
    })
    return chain_output

def filter_response(text_input):
    res = extraction_chain.run(text_input)
    print(res)
    object_maker(res)
    return res

def check_what_is_empty(flight_details):
    ask_for = []
    for field, value in flight_details.items():
        if value in [None, "", 0]:
            ask_for.append(f"{field}")
    return ask_for

def object_maker(inputstr):
    # Split the input string by spaces
    print(type(inputstr))
    # parts = inputstr.split()

    # # Create an empty dictionary
    # result_dict = {}

    # # Iterate through the parts and extract key-value pairs
    # for part in parts:
    #     key, value = part.split('=')
    #     result_dict[key] = value if value != "None" else None

    # # Now, result_dict is a dictionary with the key-value pairs
    # print(result_dict)