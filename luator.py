'''
 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                 

A script that will handle reading and outputting to a new lua file

'''

import os

class luator:

    '''The master class for luator'''
    def __init__(self, lua_file):

        self.lua_file=lua_file

        self.current_date="set_date_here"
        
        self.logo_data="set_logo_here"
        self.product_data="set_product_here"
        
        self.package_name="set_title_here"
        self.customer_sup_text="set_support_here"
        self.thanks_message="set_thanks_here"
        self.menu_instr="set_menu_text_here"

        self.fonts_message="set_font_title_here"
        self.fonts="set_font_details_here"

        self.manual_instr="set_man_title_here"
        self.manual="set_man_link_here"

        self.welcome_text_font="set_welcome_font_here"
        self.welcome_text_size=0
        self.welcome_text_style="set_welcome_style_here"
        self.welcome_text="set_welcome_here"

    
    def get_lua(self, file):

        '''
        Pass in the lua file and the file as variable
        '''
        with open(file, 'r') as lua:
            self.lua_file = lua.read()
            
            return self.lua_file
            