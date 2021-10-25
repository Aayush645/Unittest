import unittest

class testCheck(unittest.TestCase):  
           
      def test1(self):
          result=1+2+6
          self.assertEqual(result,6)


if __name__=='__main__':
     unittest.main()
