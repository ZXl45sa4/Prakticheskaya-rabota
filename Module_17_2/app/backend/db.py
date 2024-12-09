from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

# строка подключения
sqlite_database = "sqlite:///taskmanager.db"

# создаем движок SqlAlchemy
engine = create_engine(sqlite_database, echo=True)


# создаем базовый класс для моделей
class Base(DeclarativeBase): pass
