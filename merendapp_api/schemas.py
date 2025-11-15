from pydantic import  BaseModel, EmailStr

class Message(BaseModel):
    name: str
    email: EmailStr
    phone: str
    company: str
    company_type: str
    message: str
