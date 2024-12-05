from fastapi import FastAPI, status, Body, HTTPException, Path
from pydantic import BaseModel
from typing import Annotated, List, Dict

app = FastAPI()

users = []  # список users


class User(BaseModel):
    id: int = None
    username: str
    age: int


# Получение задачи по ID
@app.get("/users", response_model=list[User])
async def get_user():
    return users


# Создание новой задачи
@app.post("/user/{username}/{age}", response_model=list[User])
async def post_user(username: Annotated[str, Path(min_length=3, max_length=100)],
                    age: Annotated[int, Path()]):
    new_id = max(user.id for user in users) + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return


# Обновление задачи
@app.put("/user/{user_id}/{username}/{age}", response_model=list[User])
async def put_user(user_id: Annotated[int, Path(ge=1)],
                   username: Annotated[str, Path(min_length=3,max_length=100)],
                   age: Annotated[int, Path()], ):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="Message not found")


# Удаление задачи
@app.delete("/user/{user_id}", response_model=list[User])
async def delete_user(user_id: Annotated[int, Path(ge=1)]):
    for i in users:
        if i.id == user_id:
            users.remove(i)
            return
    raise HTTPException(status_code=404, detail="Message not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
