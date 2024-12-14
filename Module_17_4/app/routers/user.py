from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import User
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])
db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/')
#   Должна возвращать список всех пользователей из БД. Используйте scalars, select и all
async def all_users(db: db_dependency):
    users = db.scalars(select(User)).all()
    return users


@router.get("/user_id")
#   Для извлечения записи используйте ранее импортированную функцию select.
#   Дополнительно принимает user_id.
#   Выбирает одного пользователя из БД.
#   Если пользователь не None, то возвращает его.
#   В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
async def user_by_id(user_id: int, db: db_dependency):
    user = db.scalars(select(User).where(User.id == user_id)). all()
    if user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    return user


@router.post('/create')
#   Для добавления используйте ранее импортированную функцию insert.
#   Дополнительно принимает модель CreateUser.
#   Подставляет в таблицу User запись значениями указанными в CreateUser.
#   В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
#   Обработку исключения существующего пользователя по user_id или username можете сделать по желанию.
async def create_user(create_user: CreateUser, db: db_dependency):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/update")
#   Для обновления используйте ранее импортированную функцию update.
#   Дополнительно принимает модель UpdateUser и user_id.
#   Если находит пользователя с user_id, то заменяет эту запись значениям из модели UpdateUser.
#   Далее возвращает словарь {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
#   В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
async def update_user(db: db_dependency, update_user: UpdateUser, user_id: int):
    user_update = db.scalars(select(User).where(User.id == user_id))
    if user_update is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    db.execute(update(User).where(User.id == user_id).values(firstname=update_user.firstname,
                                                             lastname=update_user.firstname,
                                                             age=update_user.age))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete("/delete")
#   Для удаления используйте ранее импортированную функцию delete.
#   Всё должно работать аналогично функции update_user, только объект удаляется.
#   Исключение выбрасывать то же
async def delete_user(db: db_dependency, user_id: int):
    user_delete = db.execute(delete(User).where(User.id == user_id))
    db.commit()
    if user_delete.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task successfully deleted!'}
