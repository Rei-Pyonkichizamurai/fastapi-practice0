from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None  # 任意項目
    price: float
    is_offer: bool = False