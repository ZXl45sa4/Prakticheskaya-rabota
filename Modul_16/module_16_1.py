from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/{user_id}")
async def welcome() -> dict:
    return {"message": "Вы вошли как пользователь № <123>"}


@app.get("/user/admin")
async def welcome() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user")
async def welcome() -> dict:
    return {"message": "Информация о пользователе. Имя: <Aleksey>, Возраст: <39>"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)