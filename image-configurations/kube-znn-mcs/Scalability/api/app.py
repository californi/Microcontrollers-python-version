from fastapi import FastAPI, Request, Response
import httpx
#from pydantic import BaseModel
import asyncio

#class Message(BaseModel):
#    id: int
#    message: str

app = FastAPI()

#url_host = 'http://<service-name>:<port>'
#url_host = 'http://analyser:5001'
#microcontrollers Base64    bWljcm9jb250cm9sbGVycw==
headers = {'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}

@app.post("/decreaseScalability/")
def decreaseScalability():

    # decreaseScalability

    # updating the Knowledge

    return "empty"

@app.post("/increaseScalability/")
def increaseScalability():

    # increaseScalability

    # updating the Knowledge

    return "empty"
