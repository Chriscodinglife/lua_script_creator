'''
 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                 

A test script for ensuring the gen_lua.py script runs properly

'''

import unittest
from gen_lua import genlua


class Test_gen_lua(unittest.TestCase):

    '''
    The main test class to verify gen_lua is working properly
    '''
    gl = genlua()

    def test_read_lua(self):

        '''Ensure lua template can be read'''
        self.assertEqual(self.gl.get_lua(), "<class 'str'>")


if __name__ == '__main__':
    
    unittest.main()