'''
Created on Nov 18, 2017

@author: TZ-WORKSTATION
'''
import unittest

import mockHumiditySensor
from mockHumiditySensor import mockdata

class Test(unittest.TestCase):
    
    def testAcceptedRange(self):
        self.assertGreaterEqual( 1023, mockdata , )
        self.assertGreaterEqual(mockdata, 0,)
            

    def testTimeDelay(self):
        self.assertEqual(mockHumiditySensor.TimeDelay(), 2,)
        

    def testActive(self):
        self.assertEqual(mockHumiditySensor.isActive(), 0,)
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.teste']
    unittest.main()