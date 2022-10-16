'''

 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                                                   
Generate OBS Lua Fast API Server

- This is intended to act as a host for creating and outputting an OBS File to be used with a given Stream package

'''

from ctypes import Union
from luator import luator
from pydantic import BaseModel
from fastapi import FastAPI, status
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


class OBSFile(BaseModel):
    '''OBS File Model'''
    package_name: str
    store_name: Union[str, None] = None
    support_link: Union[str, None] = None
    manual_link: Union[str, None] = None
    logo_image: str
    product_image: str


@app.get("/ping", status_code=201)
def ping():

  '''Return a hello there for a successful ping'''
  return {"response": "Hello there"}


@app.post("/generate", status_code=status.HTTP_201_CREATED)
def generate_lua_file():

  '''Return a Lua File to download for OBS'''

  pass