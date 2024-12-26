from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *
from sqlalchemy.schema import CreateTable


class Task(Base):
    __tablename__ = "tasks"  # Имя таблицы в базе данных
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True,
                index=True)  # Уникальный идентификатор (целое число, первичный ключ, с индексом).
    title = Column(String)  # строка.
    content = Column(String)  # строка.
    priority = Column(Integer, default=0)  # целое число, по умолчанию 0.
    completed = Column(Boolean, default=False)  # булево значение, по умолчанию False.
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True,
                     index=True)  # Cвязь с Users. Целое число, внешний ключ на id из таблицы 'users', не NULL,
    # с индексом.
    slug = Column(String, unique=True, index=True)  # Человекочетаемый URL (строка, уникальная, с индексом).

    # Определяем отношение "один ко многим"
    user = relationship("User",
                        back_populates="tasks")  # объект связи с таблицей с таблицей User.


# После описания моделей попробуйте распечатать SQL запрос в консоль при помощи CrateTable
print(CreateTable(Task.__table__))
