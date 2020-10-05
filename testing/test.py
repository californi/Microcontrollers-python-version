import httpx
from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

class Message(BaseModel):
    id: int
    message: str

app = FastAPI()

#url = 'http://microcontrollers.com/selfdiagnosis/breplyingtoa'
url = 'http://selfdiagnosis.com/breplyingtoa'

@app.post("/asendingtob/")
def aSendingToB(message: Message):
    message_dict = message.dict()
    message_dict.update({"message": message.message + " from proactive monitoring" })

    response = httpx.post(url, json=message_dict)

    return response.json()