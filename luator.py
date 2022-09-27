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
    def __init__(self, lua_file):

        self.current_dir = os.path.dirname(__file__)

        self.temp_file = os.path.join(self.current_dir, "temp.lua")

        self.lua_file = self.get_lua(lua_file)

        self.current_date = "set_date_here"
        
        self.logo_data = "set_logo_here"
        self.product_data = "set_product_here"
        
        self.package_name = "set_title_here"
        self.customer_sup_text = "set_support_here"
        self.thanks_message = "set_thanks_here"
        self.menu_instr = "set_menu_text_here"

        self.fonts_message = "set_font_title_here"
        self.fonts = "set_font_details_here"

        self.manual_instr = "set_man_title_here"
        self.manual = "set_man_link_here"

        self.welcome_text_font = "set_welcome_font_here"
        self.welcome_text_size = 0
        self.welcome_text_style = "set_welcome_style_here"
        self.welcome_text = "set_welcome_here"
        
        


    
    def get_lua(self, file):

        '''
        Pass in the lua file and the file as variable and set the temp file
        '''

        with open(file, 'r') as lua:
            text = lua.read()
            
        self.update_temp_file(text)


    def lua_body(self):

        '''Return current text in the temp body'''

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

        replacement = re.sub(find_text, replacement_text, self.lua_body())
        self.update_temp_file(replacement)
