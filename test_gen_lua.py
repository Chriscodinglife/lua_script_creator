'''
 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                 

A test script for ensuring the gen_lua.py script runs properly

'''

import unittest
import gen_lua as gl


class Test_gen_lua(unittest.TestCase):

    '''
    The main test class to verify gen_lua is working properly
    '''

    def test_read_lua(self):

        '''Ensure lua template can be read'''
        self.assertEqual(gl.get_lua(), True)


if __name__ == '__main__':
    
    unittest.main()