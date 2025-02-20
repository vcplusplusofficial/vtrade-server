from sqlmodel import SQLModel, Field
from typing import Optional
from decimal import Decimal
from datetime import datetime

class TransactionBase (SQLModel):
    product_id: int
    seller_id: int
    buyer_id: str
    price: Decimal
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(default_factory=datetime.now)
    transaction_status: str = Field(default = "available")
    transaction_mode: str

class Transaction (TransactionBase, Table=True):
    __tablename__ = "transactions"
    transaction_id: Optional[int] = Field(default=None, primary_key=True)

class TransactionCreate (TransactionBase):
    pass

class TransactionRead (TransactionBase):
    transaction_id: int

    class Config:
        from_attributes = True

class TransactionUpdate(TransactionBase):
    seller_id: Optional[int] = None
    buyer_id: Optional[int] = None
    price: Optional[Decimal] = None
    modified_at: datetime = Field(default_factory=datetime.now)
    transaction_status: Optional[str] = None
    transaction_mode: Optional[str] = None

