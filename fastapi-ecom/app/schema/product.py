from pydantic import BaseModel,Field
from typing import Annotated
class Product(BaseModel):
    id:str
    sku:Annotated[str, Field(min_length=1, max_length=50, description="Stock Keeping Unit")] # string with extra constraints
    name:str
    