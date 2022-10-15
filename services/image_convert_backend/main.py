'''

 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                                                   
Image Converter Server

Server to return a base64 encoded image string

'''

from fastapi import FastAPI, status
from image_converter import ImageConverter
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/ping", status_code=201)
def ping():
  '''Ping the server'''
  return {"response": "Hello there"}


@app.post("/convert/", status_code=status.HTTP_201_CREATED)
async def convert_image(file: UploadFile = File(...)):
  '''Return an image in base64 data'''
  image_converter = ImageConverter()
  image_converter.create_image_file(file_name=file.filename, file=file.file)
  if image_converter.check_image_file(image_path=image_converter.image_path):
    image = image_converter.resize_image()
    image_base64_str = image_converter.convert_image_to_base64(image=image)
    return {"image": image_base64_str}
  else:
    return {"error": "File is not an image"}