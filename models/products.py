from sqlmodel import SQLModel, Field
from typing import Optional
from decimal import Decimal
from datetime import datetime

class ProductBase (SQLModel):
    product_name: str
    user_id: str
    description: str
    price: Decimal
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(default_factory=datetime.now)
    status: str = Field(default = "available")
    transaction_mode: str
    google_product_category: str

class Product (ProductBase, Table=True):
    __tablename__ = "products"
    product_id: Optional[int] = Field(default=None, primary_key=True)

class ProductCreate (ProductBase):
    pass

class ProductRead (ProductBase):
    product_id: id

    class Config:
        from_attributes = True

class ProductUpdate (ProductBase):
    product_name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    modified_at: datetime = Field(default_factory=datetime.now)
    status: Optional[str] = None
    transaction_mode: Optional[str] = None
    google_product_category: Optional[str] = None



