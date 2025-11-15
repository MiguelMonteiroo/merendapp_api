from dataclasses import asdict
from sqlalchemy import select

from merendapp_api.models import Message, Review
from tests.conftest import mock_db_time


def test_create_message(session, mock_db_time):
    with mock_db_time(model=Message) as time:
        new_message = Message(
            name='Teste',
            email='test@test.com',
            phone='11111111111',
            company='Teste',
            company_type='Distribuidor',
            message='Teste',
        )
        session.add(new_message)
        session.commit()

    message = session.scalar(select(Message).where(Message.name == 'Teste'))
    assert asdict(message) == {
        'id': 1,
        'name':'Teste',
        'email': 'test@test.com',
        'phone': '11111111111',
        'company': 'Teste',
        'company_type' : 'Distribuidor',
        'message' : 'Teste',
        'created_at': time
    }


def test_create_review(session, mock_db_time):
    with mock_db_time(model=Review) as time:
        new_review = Review(
            name='Teste',
            role='Tester',
            message='Estou Testando',
            rating=5,
        )
        session.add(new_review)
        session.commit()

    review = session.scalar(select(Review).where(Review.name == 'Teste'))
    assert asdict(review) == {
        'id': 1,
        'name':'Teste',
        'role': 'Tester',
        'message' : 'Estou Testando',
        'rating': 5,
        'created_at': time
    }