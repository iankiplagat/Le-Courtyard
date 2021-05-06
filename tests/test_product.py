import unittest
from app.auth.v1.model.user_model import Product
class ProductTest(unittest.TestCase):
      def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_product = Product(id=77, name="maji",description="kunywa maji",price=20.0,qty=6)
      def test_instance(self):

        self.assertTrue(isinstance(self.new_product,Product))

      def test_save_product(self):
        self.new_product.save_product()
        self.assertTrue(len(Product.query.all()) > 0)
      
     

  