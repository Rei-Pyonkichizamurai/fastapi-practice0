from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()
class Item(BaseModel):
    name:str
    price: float
    is_offer: bool=False

@app.get("/")
def read_root():
    return{"message":"hello,Fastapi!"}

@app.post("/items/")
def create_item(item: Item):
    return{
        "name": item.name,
        "price":item.price,
        "is_offer":  item.is_offer
    }

