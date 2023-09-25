
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from core.schemas import  RequestBody
from core.utils.bookingDetails import booking_details
from ai.llm import user_flight_details

load_dotenv()

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

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)