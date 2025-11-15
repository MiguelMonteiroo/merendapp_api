from http import HTTPStatus
from fastapi import FastAPI
from merendapp_api.schemas import Message

app = FastAPI()


@app.post('/messages/',status_code=HTTPStatus.CREATED)
def read_root(message: Message):
    return message
