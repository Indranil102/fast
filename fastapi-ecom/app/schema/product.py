from pydantic import BaseModel,Field,AnyUrl,field_validator,model_validator,computed_field
from typing import Annotated,Literal,Optional,List
from uuid import UUID
from datetime import datetime
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
    stock:Annotated[
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
    
    tags:Annotated[
        Optional[List[str]],
        Field(max_length=10, default=None, description="List of tags associated with the product, maximum 10 tags allowed")
    ]
    image_urls:Annotated[
        list[AnyUrl],
        Field(min_length=1, description="At least 1 image URL required")
    ]
    
    #dimension
    #seller
    created_at:datetime
    
    #any user cannot type the correct sku formate so we can use some validator to check the format of the sku and make sure it is correct
    @field_validator("sku",mode="after") #it works only single field validation
    @classmethod
    def validate_sku(cls, value:str):
        if "-" not in value:
            raise ValueError("SKU must contain a hyphen (-) separating the category and unique identifier")
        last= value.split("-")[-1]
        
        if not(len(last)==3 and last.isdigit()):
            raise ValueError("SKU must end with a 3-digit number")
        
        return value
        