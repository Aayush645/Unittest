import unittest

class testCheck(unittest.TestCase):  
           
      def test1(self):
          result=1+2+7
          self.assertEqual(result,10)


if __name__=='__main__':
     unittest.main()
