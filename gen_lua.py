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


@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/generate")
def gen_lua():

  '''
  General Run for gen_lua
  '''

  # Initiate luator
  lua = luator()

  # Test replace a text
  lua.replace_text("<package_name>", "This cool title here")
  lua_file = lua.export_via_web()
  lua.clean_up()

  return FileResponse(lua_file, media_type='application/octet-stream',filename=lua_file)