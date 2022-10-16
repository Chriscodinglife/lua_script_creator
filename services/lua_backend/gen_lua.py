'''

 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                                                   
Generate OBS Lua Fast API Server

- This is intended to act as a host for creating and outputting an OBS File to be used with a given Stream package

'''

from fastapi import FastAPI
from luator import luator
from fastapi.responses import FileResponse


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


@app.get("/ping", status_code=201)
def ping():

  '''Return a hello there for a successful ping'''
  return {"response": "Hello there"}


@app.post("/generate/", status_code=201)
def generate_lua_file():

  '''Return a Lua File to download for OBS'''

