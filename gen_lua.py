'''

 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                                                   
Generate OBS Lua

This is intended to output a lua script that can be used with OBS to create a user interface.
Ideally for creating scenes and importing items.

I am aware of some python to lua translators but my use case is somewhat specific. C'est la vie.

'''

import os
from luator import luator


def main():

  '''
  General Run for gen_lua
  '''

  # Get the location of the template.lua file
  current_dir = os.path.dirname(__file__)
  lua_template = os.path.join(current_dir, "template.lua")

  # Initiate luator
  lua = luator(lua_template)

  # Test replace a text
  lua.replace_text("<package_name>", "This cool title here")


if __name__ == '__main__':

  main()