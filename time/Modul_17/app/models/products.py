from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *


class Product(Base):
    __tablename__ = "products"
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)  # id наша колонна содержащая
    name = Column(String)   # имя равна колоне
    slug = Column(String, unique=True, index=True)  # элемент категории с несколькими параметрами
    description = Column(String)    # Описание нашего товара
    price = Column(Integer)     # прайс
    image_url = Column(String)  # ссылка на картинку
    stock = Column(Integer)     #
    category_id = Column(Integer, ForeignKey('categories.id'))
    rating = Column(Float)
    is_active = Column(Boolean, default=True)   # является категоряи активной

    category = relationship('Category', back_populates='products')


from sqlalchemy.schema import CreateTable
print(CreateTable(Product.__table__))
