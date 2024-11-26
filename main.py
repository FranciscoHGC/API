from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

items = [
    {"SKU": "104", "name": "Traditional Round Carving Board 104", "medidas": "46cm X 46cm X 3.8cm", "collecction": "Traditional Collection ", "onStockStatus": True,"image": "https://drive.google.com/file/d/1XL9rwwkZ5OQ-BMc4XgJyUjrCNacZllAo/view" },
    {"SKU": "105", "name": "Traditional Carving Board (S) 105", "medidas": "41cm X 31cm X 3.8cm", "collecction": "Traditional Collection ", "onStockStatus": False,"image": "https://drive.google.com/file/d/1XL9rwwkZ5OQ-BMc4XgJyUjrCNacZllAo/view"},
    {"SKU": "106", "name": "Traditional Cutting Board (M) 106", "medidas": "51cm X 38cm X 3.8cm", "collecction": "Traditional Collection ", "onStockStatus": True,"image": "https://drive.google.com/file/d/1XL9rwwkZ5OQ-BMc4XgJyUjrCNacZllAo/view"},
]


app = FastAPI()

#http://127.0.0.1:8000

class UpdateItem(BaseModel):
    SKU: str = None
    name: str = None
    medidas: str = None
    collecction: str = None
    onStockStatus: bool = None
    image: str = None

@app.get("/items")
def get_items():
    return {"items": items}


@app.get("/")
def index():
    return {"message" : 'Hola publico'}


@app.get("/items/{id}")
def get_item(id: int):
    if id < 0 or id >= len(items):
        return {"error": "Índice fuera de rango"}
    return {"item": items[id]}

@app.put("/items/{id}")
def update_item(id: int, item: UpdateItem):
    if id < 0 or id >= len(items):
        raise HTTPException(status_code=404, detail="Índice fuera de rango")

    # Actualizar los campos enviados en el request
    if item.SKU is not None:
        items[id]["SKU"] = item.SKU
    if item.name is not None:
        items[id]["name"] = item.name
    if item.medidas is not None:
        items[id]["medidas"] = item.medidas
    if item.collecction is not None:
        items[id]["collecction"] = item.collecction
    if item.onStockStatus is not None:
        items[id]["onStockStatus"] = item.onStockStatus

    return {"message": "Producto actualizado", "item": items[id]}
