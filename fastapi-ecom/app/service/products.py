import json
from pathlib import Path
from typing import List,Dict 

DATA_FILE= Path(__file__).parent.parent / "data" / "dummy.json"


# here we load the product form the json file and return it as a list of dictionaries
def load_products()-> List[Dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE,"r",encoding="utf-8") as file:
        return json.load(file)
    
def get_all_products()->List[Dict]:
    return load_products()

def get_product_by_id(product_id: str) -> Dict:
    
    products = load_products()
    for product in products:
        if product.get("id") == product_id:
            return product
    return None

def save_product(products: List[Dict])->None:
    with open(DATA_FILE,"w",encoding="utf-8") as file:
        json.dump(products,file,indent=2, ensure_ascii=False)