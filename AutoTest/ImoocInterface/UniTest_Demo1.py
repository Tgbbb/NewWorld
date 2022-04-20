import unittest


class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   
        print('类执行之前的方法')

    @classmethod
    def tearDownClass(cls):
        print('类之行之后的方法')

    def setUp(self):
        print('test-->setup')

    def tearDown(self):
        print('test-->teardown')

    def test1(self):
        print('这个是第一个测试方法')

    def test2(self):
        print('这个是第二个测试方法')


if __name__ == '__main__':
    unittest.main()

