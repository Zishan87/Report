import unittest
from unittest.mock import patch, MagicMock
import logging
import nose
import sys
from Services.report_manager import ReportManager

# @unittest.skip("showing class skipping")
class TestStringMethods(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.value = 2
    #
    # @classmethod
    # def tearDownClass(cls):
    #     del cls.value

    # @unittest.skip("showing class skipping")
    def setUp(self):
        self.value = 2

    @unittest.skip("demonstrating skipping")
    def test_widget_quality(self):
        self.assertEqual(self.value, 5)

    # @unittest.skipIf(nose.__version__ < str(3), "not supported in this library version")
    def test_widget_operational_equality(self):
        self.assertEqual(self.value, 3+2)

    # @unittest.skipUnless(sys.platform.startswith("uni"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def ownCondition():
        if 4 == 5:
            return lambda func: func
        return unittest.skip("doesn't have {}".format(4))

    @ownCondition()
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def functi(self):
        return self.value

    def test_func(self):
        self.assertEqual(self.functi(), 2)

    def tearDown(self):
        del self.value

    def test_log(self):
        with self.assertLogs('foo', level='INFO') as cm:
            logging.getLogger('foo').info('first message')
            logging.getLogger('foo.bar').error('second message')
        self.assertEqual(cm.output, ['INFO:foo:first message',
                                     'ERROR:foo.bar:second message'])

    # def check_even(self,n, nn):
    #     assert n % 2 == 0 or nn % 2 == 0
    #
    # def test_evens(self):
    #     for i in range(0, 5):
    #         yield self.check_even, i, i * 3


class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

    def test_mock_patch(self):
        foo = {'key': 'value'}
        original = foo.copy()
        with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
            assert foo == {'newkey': 'newvalue'}
        assert foo == original


class ExpectedFailureTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

def get_mssql_patch(query_results):
    mock_dir_fmt = '__enter__.return_value.cursor.return_value.__enter__.return_value.{}'
    kwargs = {mock_dir_fmt.format(method): result for method, result in query_results.items()}
    return patch('pymssql.connect', autospec=True, return_value=MagicMock(**kwargs))

get_mssql_patch({'fetchall.return_value': []})

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_widget_quality'))
    suite.addTest(TestStringMethods('test_widget_operational_equality'))
    suite.addTest(TestStringMethods('test_windows_support'))
    suite.addTest(ExpectedFailureTestCase('test_fail'))
    suite.addTest(TestStringMethods('test_func'))
    return suite

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
    unittest.main()