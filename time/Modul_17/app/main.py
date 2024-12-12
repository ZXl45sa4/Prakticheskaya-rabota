from fastapi import FastAPI
from routers import category
from routers import products

app = FastAPI()


# базовая страничка
@app.get("/")
async def welcome():
    return {"message": "My shop"}

app.include_router(category.router)
app.include_router(products.router)
#python -m uvicorn main:app