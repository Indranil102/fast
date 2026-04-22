from fastapi import FastAPI, HTTPException, Query, Path
from app.service.products import get_all_products, get_product_by_id, add_product
from app.schema.product import Product
from uuid import uuid4
from datetime import datetime
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
    ),
    limit: int =Query(
        default=5, 
        gt=0,
        le=100,
        description="Limit the number of products returned"
    ),
    offset: int =Query(
        default=0, 
        gt=0,
        
        description="Pagination offset"
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
    products=products[offset:offset+limit]
    return {"total": total,"limit":limit, "products": products}


@app.get("/products/{products_id}")
def get_single_product(products_id:str= Path(..., min_length=36, max_length=36, description="UUID of the product"),example="8d75r78f-6835-450d-a3bc-118a60f71b91"):
    product = get_product_by_id(products_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
    


@app.post("/products",status_code=201)
def create_product(product:Product):
    product_dict=product.model_dump(mode="json")
    
    product_dict["id"]= str(uuid4())
    product_dict["created_at"]=datetime.utcnow().isoformat() + "Z"
    
    try:
        add_product(product_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return product.model_dump(mode="json")