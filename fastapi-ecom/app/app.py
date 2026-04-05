from fastapi import FastAPI, HTTPException, Query
from app.service.products import get_all_products
app= FastAPI()

@app.get("/")
def home():
    return {"message":"hii"}

# @app.get("/products")
# def get_products():
#     return get_all_products()

@app.get("/products")
def get_products(name:str=Query(default=None, min_length=3, max_length=50, description="Search by product name (case insensitive)")
                 ):
    products= get_all_products()
    if name:
        needle= name.strip().lower().strip('"')
        products= [p for p in products if needle in p.get("name","").lower()]
        
        if not products:
            raise HTTPException(status_code=404, detail="No products found matching the search criteria")
    
    total = len(products)
    return {"total": total, "products": products}