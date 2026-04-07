from fastapi import FastAPI, HTTPException, Query
from app.service.products import get_all_products
app= FastAPI()

@app.get("/")
def home():
    return {"message":"hii"}


@app.get("/products")
#hwere i can sort the thing with name and price 
def get_products(
    name:str=Query(
        default=None, 
        min_length=1, 
        max_length=50, 
        description="Search by product name (case insensitive)"
        ),
    sort_price:bool=Query(
        default=False,
        description="Sort products by price (ascending)"
    ),
    order: str=Query(
        default="asc",
        description="Sort order: 'asc' for ascending, 'desc' for descending",
    )
                 ):
    products= get_all_products()
    if name:
        needle= name.strip().lower().strip('"')
        products= [p for p in products if needle in p.get("name","").lower()]
        
    if not products:
        raise HTTPException(status_code=404, detail="No products found matching the search criteria")
            
    if sort_price:
        reverse= order.lower() == "desc"
        products=sorted(products,key=lambda x: x.get("price",0), reverse=reverse)
    
    total = len(products)
    return {"total": total, "products": products}