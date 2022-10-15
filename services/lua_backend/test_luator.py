'''
 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                 

A test script for ensuring the gen_lua.py script runs properly

'''

import os
import unittest
from luator import luator

lua = luator()

class Test_luator(unittest.TestCase):

    '''
    The main test class to verify Luator is working properly
    '''
    
    def test_clean_up(self):
        '''Pass if luator can remove the temp file and there is no longer any temp file'''
        self.assertTrue(lua.clean_up())


    def test_autput_file(self):
        '''Pass if luator can export a file to a given directory'''
        path = "~/Desktop/"
        folder_path = os.path.expanduser(path)
        message = "File could not be exported"
        self.assertTrue(lua.export_lua(folder_path), message)


if __name__ == '__main__':
    
    unittest.main()