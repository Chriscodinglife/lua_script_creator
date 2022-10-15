'''

This script is for converting images to base64 format.

'''

import base64
import pathlib
from tempfile import SpooledTemporaryFile
from PIL import Image
from io import BytesIO


class ImageConverter:
    
    '''The Image Converter Class'''

    def __init__(self):

        '''Set the initial values'''
            
        self.file_name = ""
        self.image_path = ""

    
    def create_image_file(self, file_name=str, file=SpooledTemporaryFile):

        '''Create a file with the given name and content'''

        with open(file_name, "wb") as file_object:
            file_object.write(file.read())
            self.image_path = file_name
            self.file_name = file_name

        
    def check_image_file(self, image_path=str):

        '''Check if the file is an image'''

        if pathlib.Path(image_path).suffix in [".jpg", ".jpeg", ".png"]:
            return True
        else:
            pathlib.Path(image_path).unlink()
            return False

    
    def resize_image(self):

        '''This function will resize the inputted the image to a smaller size'''

        resize_x = int(480)
        resize_y = int(270)

        original_image = Image.open(self.image_path)

        new_image = original_image.resize((resize_x, resize_y))
        original_image.close()

        return new_image
    

    def convert_image_to_base64(self, image=Image):

        '''Convert the image to base64 format'''
        buffered = BytesIO()

        image.save(buffered, format='PNG')
        image.close()
        image_base64_str = base64.b64encode(buffered.getvalue()).decode()
        
        data_image_str = "data:image/png;base64,"
        
        pathlib.Path(self.image_path).unlink()
        return data_image_str + image_base64_str