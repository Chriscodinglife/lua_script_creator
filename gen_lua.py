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

from luator import luator


def main():

  '''
  General Run for gen_lua
  '''

  # Initiate luator
  lua = luator()

  # Test replace a text
  lua.replace_text("<package_name>", "This cool title here")
  lua.export_lua()
  lua.clean_up()


if __name__ == '__main__':

  main()