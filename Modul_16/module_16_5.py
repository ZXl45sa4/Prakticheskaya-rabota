from fastapi import FastAPI, status, Body, HTTPException, Request, Form, Path  # Request - запрос
from fastapi.responses import HTMLResponse  # Response - ответ
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates

#app = FastAPI()
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")

#users = []  # список users


class User(BaseModel):
    id: int = None
    username: str
    age: int


users: List[User] =[
    User(id=1, username='UrbanUser', age=24),
    User(id=2, username='UrbanTest', age=24),
    User(id=3, username='Copybara', age=60)
]


@app.get("/")
async def get_all_messages(
    request: Request
) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_user(
    request: Request,
    user_id: Annotated[int, Path()]
) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(
    request: Request,
    user_id: Annotated[int, Path(ge=1)]
) -> str:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return f"Message with {user_id} was deleted."
    raise HTTPException(status_code=404, detail="Message not found")


@app.post('/user/{username}/{age}')
async def post_user(
        request: Request,
        username: Annotated[str, Path(min_length=3, max_length=100)],
        age: Annotated[int, Path()]
) -> HTMLResponse:
    new_id = max(user.id for user in users) + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(
        request: Request,
        user_id: Annotated[int, Path(ge=1)],
        username: Annotated[str, Path(min_length=3,max_length=100)],
        age: Annotated[int, Path()]
) -> str:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return "Message updated."
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8040)
