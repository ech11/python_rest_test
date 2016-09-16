import vroom
import os, sys
import unittest
import tempfile


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_address(self):
        res = vroom.get_address('40.7402332', '-73.99000049999999')
        print(sys._getframe().f_code.co_name, res.data)
        assert 'comment' in res.data
        assert 'address' in res.data

    def test_get_bad_address(self):
        res = vroom.get_address('-40.7402332', '-73.99000049999999')
        print(sys._getframe().f_code.co_name, res.data)
        assert 'comment' in res.data
        assert 'address' in res.data

if __name__ == '__main__':
    unittest.main()
