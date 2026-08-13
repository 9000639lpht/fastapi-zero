from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    msg: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserSchema(UserPublic):
    password: str


class Userdb(UserSchema):
    id: int
