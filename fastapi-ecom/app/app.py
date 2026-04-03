from fastapi import FastAPI, HTTPException
from app.service.products import get_all_products
app= FastAPI()

@app.get("/")
def home():
    return {"message":"hii"}

@app.get("/products")
def get_products():
    return get_all_products()