from pydantic import BaseModel,Field
from typing import Annotated,Literal
from uuid import UUID
class Product(BaseModel):
    id:UUID
    sku:Annotated[
        str, 
        Field(min_length=1,
              max_length=50,
              description="Stock Keeping Unit")] # string with extra constraints
    name:Annotated[
        str,
        Field(min_length=1, 
             max_length=100,
             title="Product Name",
             description="Name of the product")
        ]
    description:Annotated[
        str,
        Field(min_length=5,
              max_length=500,
              description="Detailed description of the product")
    ]
    
    category:Annotated[
        str,
        Field(min_length=1,
              max_length=50,
              description="Category of the product")
    ]
    
    brand:Annotated[
        str,
        Field(min_length=1,     
              max_length=50,
              description="Brand of the product")
        
    ]
    price:Annotated[
        float,
        Field(gt=0,description="Price of the product, must be greater than zero",
              strict=True)
    ]
    currency:Literal["INR"]="INR",
    discount_percentage:Annotated[
        float,
        Field(ge=0, le=100, description="Discount percentage, must be between 0 and 100", strict=True)
    ]=0.0  
    stock=Annotated[
        int,
        Field(ge=0, description="Available stock quantity, must be non-negative")
    ]
    is_active:Annotated[
        bool,
        Field(description="Indicates if the product is active and available for purchase")
    ]
    rating:Annotated[
        float,
        Field(ge=0, le=5, description="Average customer rating, must be between 0 and 5", strict=True)
    ]=0.0