import unittest

class testCheck(unittest.TestCase):  
           
      def test1(self):
          result=1+2+8
          self.assertEqual(result,11)


if __name__=='__main__':
     unittest.main()
