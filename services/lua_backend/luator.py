'''
 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                 

A script that will handle reading and outputting to a new lua file

'''
import os
import re

class luator:

    '''The master class for luator'''
    def __init__(self, lua_file=None):

        self.current_dir = os.path.dirname(__file__)
        self.lua_template = os.path.join(self.current_dir, "template.lua")

        self.temp_file = ""

        if lua_file != None:
            self.get_lua(lua_file)
        else:
            self.get_lua(self.lua_template)

        self.obs_data = {'package_name': "",
                        'store_name': "",
                        'support_link': "",
                        'manual_link':  "",
                        'logo_image': "",
                        'product_image': '',}

        self.obs_replace = {'package_name': "<package_name>",
                            'store_name': "<store_name>",
                            'support_link': "<support_link>",
                            'manual_link':  "<manual_link>",
                            'logo_image': "<logo_image>",
                            'product_image': '<product_image>',}

        self.output_file_name = "Quick OBS Installer.lua"
   
        
    def get_lua(self, file):

        '''
        Pass in the given file and make a temporary copy of it
        '''

        if self.check_lua(file):

            self.temp_file = os.path.join(self.current_dir, "temp.lua")
            
            with open(file, 'r') as lua:
                text = lua.read()
                
                self.update_temp_file(text)
                return True


    def temp_body(self):

        '''Return current text in the temp body'''

        if self.check_temp():
            with open(self.temp_file, 'r') as lua:
                return lua.read()


    def update_temp_file(self, new_text):

        '''
        Create a new temp file of the lua file in the current directory
        '''

        if new_text != "":
                
            with open(self.temp_file, 'w') as lua:
                lua.write(new_text)
                return True
    

    def replace_text(self, find_text, replacement_text):

        '''
        Pass in the text that needs to be replaced, and swap it for the replacement
        Ensure to use regex for the find_text variable
        '''

        replacement = re.sub(find_text, replacement_text, self.temp_body())
        self.update_temp_file(replacement)

    
    def set_obs_data(self, data):
        '''
        Pass in a dictionary of the OBS data
        '''
        for key in data:
            self.obs_data[key] = data[key]

    
    def replace_obs(self):

        '''
        Replace the values in the OBS file with given OBS Data
        '''
        for key in self.obs_data:
            if self.obs_data[key] != "":
                self.replace_text(self.obs_replace[key], self.obs_data[key])

    
    def check_lua(self, file_path):

        '''
        Pass in the file path and return true if file is not a .lua file
        '''

        if file_path:
            extension = os.path.splitext(file_path)[-1].lower()

            if extension == ".lua":
                
                return True
        
            raise NotLuaFile(file_path)

    
    def check_temp(self):
        
        '''
        Return true if the temp file exists
        '''
        if os.path.exists(self.temp_file):
            return True
        raise NoTempFile(self.temp_file)


    def set_template(self):

        '''
        Set the template file as the lua and return True
        '''
        self.get_lua(self.lua_template)

    
    def export_lua_local_test(self, given_path=None):
        
        '''
        Request the location of the output path from the user
        '''
        if given_path == None:
            output_path = input('Enter in the path to Export the Lua file: ').replace('"', "")
            if output_path == "":
                output_path = os.path.expanduser("~/Desktop/")
        else:
            output_path = given_path
        
        normal_path = os.path.normpath(output_path)
        full_path = os.path.join(normal_path, self.output_file_name)

        if self.check_temp():
            with open(self.temp_file, 'r') as read_lua:
                body = read_lua.read()


        with open(full_path, 'w') as output_file:
            output_file.write(body)

            return True

    
    def export_via_web(self):
        '''
        Create the final lua file and return the file
        '''

        if self.check_temp():
            with open(self.temp_file, 'r') as read_temp:
                temp_body = read_temp.read()
                
            with open(self.output_file_name, 'w') as output_file:
                output_file.write(temp_body)

            return self.output_file_name

    
    def clean_up(self):

        '''
        Pass True after removing the temp file
        '''
        try:
            os.remove(self.temp_file)
        except Error as error:
            print(error)
            return True

        if os.path.exists(self.temp_file) and os.path.exists(self.output_file_name):
            return False
        return True


class Error(Exception):
    '''Base class for other exceptions'''
    pass


class NotLuaFile(Error):
    '''
    Raise when file is not a lua file
    '''
    def __init__(self, file_path):
        self.file_path = file_path
        self.message = f"{self.file_path} is not a lua file. Please pass in a lua file"
        super().__init__(self.message)


class NoTempFile(Error):
    '''
    Raise when temp file does not exist
    '''
    def __init__(self, file_path):
        self.file_path = file_path
        self.message = f"{self.file_path} does not exist. Make sure to either set the template or pass in a lua file."
        super().__init__(self.message)