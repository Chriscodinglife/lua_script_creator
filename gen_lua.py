'''

 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                                                   
Generate OBS Lua Fast API Server

- This is intended to act as a host for creating and outputting an OBS File to be used with a given Stream package

'''

from typing import Union
from fastapi import FastAPI
from luator import luator
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


def gen_lua():

  '''
  General Run for gen_lua
  '''

  # Initiate luator
  lua = luator()

  # Test replace a text
  lua.replace_text("<package_name>", "This cool title here")
  lua.export_lua()
  lua.clean_up()


# if __name__ == '__main__':

#   main()