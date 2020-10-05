from fastapi import FastAPI, Request, Response
import httpx
from pydantic import BaseModel
import asyncio

class Message(BaseModel):
    id: int
    message: str

app = FastAPI()

#url = 'http://selfdiagnosis.com/breplyingtoa'
#url_host = 'http://<service-name>:<port>'
url_host = 'http://selfdiagnosis-service:5001'
#microcontrollers Base64    bWljcm9jb250cm9sbGVycw==
headers = {'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}

@app.post("/asendingtob/")
def aSendingToB(message: Message):

    message_dict = message.dict()

    # Requesting self-diagnosis

    message_dict.update({"message": message.message + " from proactive monitoring" })

    response = httpx.post(f"{url_host}/breplyingtoa", 
        headers=headers, 
        json=message_dict) 

    return response.text