from flask import jsonify
import flask_unittest
from app.config import Config
from app import create_app, db


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None


class ApiTest(flask_unittest.ClientTestCase):
    API_URL = 'http://127.0.0.1:5000/api'
    CATEGORY_URL = f'{API_URL}/category'
    CATEGORIES_URL = f'{API_URL}/categories'
    PRODUCT_URL = f'{API_URL}/product'
    PRODUCTS_URL = f'{API_URL}/products'
    SUM_URL = f'{CATEGORY_URL}/sum'
    SEARCH_URL = f'{API_URL}/search'
    CATEGORY_OBJ = {
        'title': 'category_test_title',
        'description': 'category_test_description',
        'id': 1,
        'products': []
    }
    PRODUCT_OBJ = {
        'title': 'product_test_title',
        'price': 100.0,
        'description': 'product_test_description',
        'sales_start': '2023-01-01',
        'amount': 3000,
        'category_id': 1,
        'id': 1,
        'img_path': './static/images/products/default.jpg'
    }

    app = create_app(TestConfig)
    app_context = app.app_context()

    @classmethod
    def setUpClass(cls):
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_01_post_category(self, client):
        """POST request to /api/category; adds new item to database"""
        res = client.post(self.CATEGORY_URL, data=self.CATEGORY_OBJ)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, self.CATEGORY_OBJ)

    def test_02_post_product(self, client):
        """POST request to /api/product; adds new item to database"""
        res = client.post(self.PRODUCT_URL, data=self.PRODUCT_OBJ)
        self.CATEGORY_OBJ['products'].append(self.PRODUCT_OBJ)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, self.PRODUCT_OBJ)

    def test_03_get_category(self, client):
        """GET request to /api/category; returns the details of certain category by id parameter"""
        res = client.get(self.CATEGORY_URL, query_string={'id': 1})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, self.CATEGORY_OBJ)

    def test_04_put_category(self, client):
        """PUT request to /api/category with only 1 parameter (title) changes an item in database"""
        res = client.put(self.CATEGORY_URL, data={'id': 1, 'title': 'category_test_put'})
        new_category = self.CATEGORY_OBJ
        new_category['title'] = 'category_test_put'
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, new_category)

    def test_05_put_category(self, client):
        """PUT request to /api/category with all possible parameters; changes an item in database"""
        res = client.put(self.CATEGORY_URL, data={'id': 1} | self.CATEGORY_OBJ)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, self.CATEGORY_OBJ)

    def test_06_get_all_categories(self, client):
        """GET request to /api/categories; gets all categories from database"""
        res = client.get(self.CATEGORIES_URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, [self.CATEGORY_OBJ])

    def test_07_get_product(self, client):
        """GET request to /api/product; returns the details of certain product by id parameter"""
        res = client.get(self.PRODUCT_URL, query_string={'id': 1})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, self.PRODUCT_OBJ)

    def test_08_put_product(self, client):
        """PUT request to /api/product with only 1 parameter (title); changes an item in database"""
        res = client.put(self.PRODUCT_URL, data={'id': 1, 'title': 'product_test_put'})
        new_product = self.PRODUCT_OBJ
        new_product['title'] = 'product_test_put'
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, new_product)

    def test_09_put_product(self, client):
        """PUT request to /api/product with all possible parameters; changes an item in database"""
        res = client.put(self.PRODUCT_URL, data={'id': 1} | self.PRODUCT_OBJ)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, self.PRODUCT_OBJ)

    def test_10_get_all_products(self, client):
        """GET request to /api/products; gets all products from database"""
        res = client.get(self.PRODUCTS_URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, [self.PRODUCT_OBJ])

    def test_11_category_sum(self, client):
        """GET request to /api/category/sum; returns the sum of all products in the certain category"""
        res = client.get(self.SUM_URL, query_string={'id': 1})
        result = {'sum': self.PRODUCT_OBJ['amount']}
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, result)

    def test_12_search(self, client):
        """GET request to /api/search; returns products, available by certain date"""
        res = client.get(self.SEARCH_URL, query_string={'date': '2023-03-20'})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, [self.PRODUCT_OBJ])

    def test_13_delete_product(self, client):
        """DELETE request to /api/product; deletes item from database"""
        res = client.delete(self.PRODUCT_URL, data={'id': 1})
        self.CATEGORY_OBJ['products'].pop()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, self.PRODUCT_OBJ)

    def test_14_delete_category(self, client):
        """DELETE request to /api/category; deletes item from database"""
        res = client.delete(self.CATEGORY_URL, data={'id': 1})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, self.CATEGORY_OBJ)


"""if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ApiTest('rest_test'))
    runner = unittest.TextTestRunner()
    runner.run(suite)"""
