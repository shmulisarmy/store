from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from time import sleep

from data import store_items, full_data

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items": store_items})


@app.get("/api/store_items")
async def get_store_items():
    sleep(2)
    return store_items


@app.get("/api/store_items/{item_id}")
async def get_store_item(item_id: int):
    if item_id not in full_data:
        raise ValueError("Item not found")
    
    return full_data[item_id]
