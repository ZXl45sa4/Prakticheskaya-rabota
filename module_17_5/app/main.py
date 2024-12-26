from fastapi import FastAPI
from app.routers import task, user
from app.backend.db import engine, Base

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


# Подключаем роутеры
app.include_router(user.router)
app.include_router(task.router)

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

# python -m uvicorn main:

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8004)
