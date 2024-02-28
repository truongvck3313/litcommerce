import litcommerce1
import unittest






class Test(unittest.TestCase):
    def test_login(self):
        litcommerce1.login(self)
        litcommerce1.test(self)


if __name__ == "__main__":
    unittest.main()




