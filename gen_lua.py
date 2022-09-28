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