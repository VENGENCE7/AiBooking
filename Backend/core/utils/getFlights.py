from datetime import datetime
import requests


def get_flight_in_period(fly_from, fly_to, date_from, date_to, sort):
    try:
        headers = {"apikey": "0tvfUPHxSK3axHyPv0wOlCKPcwcF-T7f"}
        BASE_URL = f'https://api.tequila.kiwi.com/v2/search?fly_from={fly_from}&fly_to={fly_to}&date_from={date_from}&date_to={date_to}&sort={sort}&limit=5&curr=AUD'
        response = requests.get(BASE_URL, headers=headers)
        response = response.json()
        flights = []
        for flight in response['data']:
            price = flight['price']
            duration = flight['duration']['departure']/3600
            availability = flight['availability']["seats"]
            routes = flight['route']
            departure= datetime.fromisoformat(flight['local_departure'][:-1])
            arrival=datetime.fromisoformat(flight['local_arrival'][:-1])
            details = []
            for idx, route in enumerate(routes):
                singleRoute={
                    "index":idx,
                    "route":route['airline'],
                    "flightNo":route['flight_no'],
                    "from":f"{route['cityFrom']}",
                    "to":f"{route['cityTo']}"
                }
                details.append(singleRoute)

            flight_info = {
                "price": price,
                "duration": duration,
                "availability": availability,
                "departure":departure.strftime("%b %d, %Y %I:%M %p"),
                "arrival":arrival.strftime("%b %d, %Y %I:%M %p"),
                "routes": details
            }
            flights.append(flight_info)
        return flights
    except:
        print("An exception occurred")