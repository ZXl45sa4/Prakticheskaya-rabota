from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *
from sqlalchemy.schema import CreateTable


class User(Base):
    __tablename__ = "users" # Имя таблицы в базе данных
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True,
                index=True)  # Уникальный идентификатор (целое число, первичный ключ, с индексом).
    username = Column(String)  # строка.
    firstname = Column(String)  # строка.
    lastname = Column(String)  # строка.
    age = Column(Integer)  # целое число.
    slug = Column(String, unique=True, index=True)  # строка, уникальная, с индексом.

    # Определяем отношение "Многие к одному"
    tasks = relationship("Task",
                         back_populates="user")  # объект связи с таблицей с таблицей Task.


# После описания моделей попробуйте распечатать SQL запрос в консоль при помощи CrateTable
print(CreateTable(User.__table__))
