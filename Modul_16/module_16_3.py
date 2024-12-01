from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_user() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    current_user = str(int(max(users, key=int)) + 1)
    users[current_user] = f"Имя:{username}, возраст: {age}"
    return "User <user_id> is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: int, username: Annotated[str, Path(min_length=5, max_length=20
    , description="Enter username"
    , example="UrbanUser")], age: Annotated[int, Path(ge=18, le=120
    , description="Enter age", example="24")]) -> str:
    users[user_id] = f"Имя:{username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    #del users[user_id]
    users.pop(user_id)
    return f"User {user_id} has been deleted"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
