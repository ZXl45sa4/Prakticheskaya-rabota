from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import User
from app.models import Task
from app.schemas import CreateUser, UpdateUser, CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/")
#   Должна возвращать список всех пользователей из БД. Используйте scalars, select и all
async def all_tasks(db: db_dependency):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get("/task_id")
#   Для извлечения записи используйте ранее импортированную функцию select.
#   Дополнительно принимает user_id.
#   Выбирает одного пользователя из БД.
#   Если пользователь не None, то возвращает его.
#   В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
async def task_by_id(task_id: int, db: db_dependency):
    task = db.scalars(select(Task).where(Task.id == task_id)). all()
    if task is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task was not found')
    return task


@router.post("/create")
#   Дополнительно принимает модель CreateTask и user_id.
#   Подставляет в таблицу Task запись значениями указанными в CreateUser и user_id, если пользователь найден.
#   Т.е. при создании записи Task вам необходимо связать её с конкретным пользователем User.
#   В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
#   В случае отсутствия пользователя выбрасывает исключение с кодом 404 и описанием "User was not found"
async def create_task(create_task: CreateTask, db: db_dependency, task_id: int, user_id: int):
    user_update = db.scalars(select(User).where(User.id == user_id))
    if user_update is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    db.execute(insert(Task).values(title=create_task.title,
                                   content=create_task.content,
                                   priority=create_task.priority,
                                   user_id=create_task.user.id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/update")
#   Для обновления используйте ранее импортированную функцию update.
#   Дополнительно принимает модель UpdateUser и user_id.
#   Если находит пользователя с user_id, то заменяет эту запись значениям из модели UpdateUser.
#   Далее возвращает словарь {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
#   В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
async def update_task(db: db_dependency, update_task: UpdateTask, task_id: int):
    task_update = db.scalars(select(Task).where(Task.id == task_id))
    if task_update is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    db.execute(update(Task).where(Task.id == task_id).values(title=update_task.title,
                                                             content=update_task.content,
                                                             priority=update_task.priority))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete("/delete")
#   Для удаления используйте ранее импортированную функцию delete.
#   Всё должно работать аналогично функции update_user, только объект удаляется.
#   Исключение выбрасывать то же
async def delete_task(db: db_dependency, task_id: int):
    task_delete = db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    if task_delete.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task successfully deleted!'}


@router.delete("/all_delete")
async def delete_all_task(db: db_dependency):
    task_delete = db.execute(delete(Task))
    db.commit()
    if task_delete.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task successfully deleted!'}
