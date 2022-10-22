'''

 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                                                   
Generate OBS Lua Fast API Server

- This is intended to act as a host for creating and outputting an OBS File to be used with a given Stream package

'''

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
    store_name: str
    support_link: str
    manual_link: str
    logo_image: str
    product_image: str


@app.get("/ping", status_code=201)
def ping():

  '''Return a hello there for a successful ping'''
  return {"response": "Hello there"}


@app.post("/generate", status_code=status.HTTP_201_CREATED)
async def generate_lua_file(obsfile: OBSFile):

  '''Return a Lua File to download for OBS'''

  data = {'package_name': obsfile.package_name,
                'store_name': obsfile.store_name,
                'support_link': obsfile.support_link,
                'manual_link':  obsfile.manual_link,
                'logo_image': obsfile.logo_image,
                'product_image': obsfile.product_image,}

  lua = luator()
  lua.set_obs_data(data)
  lua.replace_obs()
  lua_file = lua.export_via_web()
  outputfile_name = "Quick OBS Installer.lua"

  headers = {'Access-Control-Expose-Headers': 'Content-Disposition'}
  return FileResponse(lua_file, filename=outputfile_name, headers=headers)