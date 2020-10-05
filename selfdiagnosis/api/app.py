from fastapi import FastAPI, Request
import httpx
from pydantic import BaseModel

class Message(BaseModel):
    id: int
    message: str

app = FastAPI()

@app.post("/breplyingtoa")
async def BReplyingToA(message: Message):

    # Requesting self-diagnosis
    messageReturn = {
        'id': message.id, 
        'message': message.message + ' - Message from Selfdiagnosis'
    }


    return messageReturn

