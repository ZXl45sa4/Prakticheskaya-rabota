from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models import *
from sqlalchemy import insert
from app.schemas import CreateCategory

from slugify import slugify
from sqlalchemy import select
from sqlalchemy import update

router = APIRouter(prefix="/category", tags=["category"])


@router.post("/create")
async def creaty_category(db: Annotated[Session, Depends(get_db)], create_category: CreateCategory):
    db.execute(insert(Category).values(name=create_category.name,  # db.execute писали в sqlite с execute
                                       parent_id=create_category.parent_id,
                                       slug=slugify(create_category.name)))  # slugify код для с сылки генерируем при
    # помощи библиотеки slugify эта штука позволяет нам убрать лишние пробелы в целом приводить обыкновенную строку в
    # слагоподоьный вид, что очень удобно
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


# -------------------------------------------------


@router.get("/all_categories")
async def get_all_categories(db: Annotated[Session, Depends(get_db)]):
    categories = db.scalars(select(Category).where(Category.is_active == True)).all()
    return categories


# -------------------------------------------------


@router.put("/update_category")
async def update_category(db: Annotated[Session, Depends(get_db)], category_id: int, update_category: CreateCategory):
    category = db.scalars(select(Category).where(Category.id == category_id))
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no category found'
        )

    db.execute(update(Category).where(Category.id == category_id).values(
        name=update_category.name,
        slug=slugify(update_category.name),
        parent_id=update_category.parent_id))

    db.commit() # Сохроняем состояние
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Product update is successful'
    }
#-------------------------------------------------------------


@router.delete("/delete")
async def delete_category(db: Annotated[Session, Depends(get_db)], category_id: int):
    category = db.scalars(select(Category).where(Category.id == category_id))
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no category found'
        )
    db.execute(update(Category).where(Category.id == category_id).values(is_active=False))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Product update is successful'
    }
