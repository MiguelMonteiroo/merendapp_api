from http import HTTPStatus

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from merendapp_api.database import get_session
from merendapp_api.models import Message, Review
from merendapp_api.schemas import MessageSchema, ReviewSchema

app = FastAPI()


@app.post('/messages/', status_code=HTTPStatus.CREATED)
def create_message(
    message: MessageSchema, session: Session = Depends(get_session)
):

    message = Message(
        message.name,
        str(message.email),
        message.phone,
        message.company,
        message.company_type,
        message.message,
    )
    session.add(message)
    session.commit()
    session.refresh(message)

    return message


@app.post('/reviews/', status_code=HTTPStatus.CREATED)
def create_review(
    review: ReviewSchema, session: Session = Depends(get_session)
):

    review = Review(review.name, review.role, review.message, review.rating)
    session.add(review)
    session.commit()
    session.refresh(review)

    return review
