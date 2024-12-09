from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: str


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: str


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int