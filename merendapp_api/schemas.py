from pydantic import BaseModel, EmailStr


class MessageSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str
    company: str
    company_type: str
    message: str


class ReviewSchema(BaseModel):
    name: str
    role: str
    message: str
    rating: int


class ReviewDB(ReviewSchema):
    id: int


class MessageDB(MessageSchema):
    id: int
