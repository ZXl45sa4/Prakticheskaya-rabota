from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///taskmanager.db"  # Путь к базе данных SQLite

# Создаем движок для подключения к базе данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

# Создаём фабрику сессий для работы с базой данных
SessionLocal = sessionmaker(autoflush=False, bind=engine)


# создаем базовый класс для моделей
class Base(DeclarativeBase):
    pass

# async def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
