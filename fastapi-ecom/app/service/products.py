import json
from pathlib import Path
from typing import List,Dict 

DATA_FILE= Path("..","data","products.json")


# here we load the product form the json file and return it as a list of dictionaries
def load_products()-> List[Dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE,"r","utf-8") as file:
        return json.load(file)