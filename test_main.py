import litcommerce
import unittest






class Test(unittest.TestCase):
    def test_login(self):
        litcommerce.login(self)
        litcommerce.test(self)


if __name__ == "__main__":
    unittest.main()




