from fastapi import FastAPI, status, Body, HTTPException, Path
from pydantic import BaseModel
from typing import Annotated, List, Dict

app = FastAPI()

users = []  # список users


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users", response_model=list[User])
async def get_user() -> list[User]:
    return users


@app.post("/user", response_model=list[User])
async def post_user(user: User) -> User:
    user.id = len(users) + 1
    users.append(user)
    return user


@app.put("/user/{user_id}", response_model=list[User])
async def put_user(user_id: int, task: User = Body()) -> User:
    for t in users:
        if t.id == user_id:
            t.username = task.username
            t.age = task.age
            return t
    raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/user/{user_id}", response_model=list[User])
async def delete_user(user_id: int) -> dict[str, str]:
    for i, t in enumerate(users):
        if t.id == user_id:
            del users[i]
            return {"detail": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Message not found")

if __name__ == "__main_1__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
