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
    
    def test_output_file(self):
        '''Pass if luator can export a file to a given directory'''
        path = "~/Desktop/"
        folder_path = os.path.expanduser(path)
        message = "File could not be exported"
        self.assertTrue(lua.export_lua(folder_path), message)


if __name__ == '__main__':
    
    unittest.main()