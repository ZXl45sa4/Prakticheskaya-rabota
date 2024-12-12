from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
#Column - колонна, ForeignKey - указатель на ячейку
from sqlalchemy.orm import relationship
# relationship - взаимосвязь
from app.models import *


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)  # unique=True(уникальный элемент)
    is_active = Column(Boolean, default=True)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable="category")

    products = relationship("Product", back_populates="category")


from sqlalchemy.schema import CreateTable
print(CreateTable(Category.__table__))