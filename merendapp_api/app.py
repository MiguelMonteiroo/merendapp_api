from http import HTTPStatus

from fastapi import FastAPI

from merendapp_api.schemas import MessageDB, MessageSchema

app = FastAPI()

database = []


@app.post('/messages/', status_code=HTTPStatus.CREATED)
def create_message(message: MessageSchema):
    message_with_id = MessageDB(**message.model_dump(), id=len(database) + 1)
    database.append(message_with_id)

    return message_with_id
