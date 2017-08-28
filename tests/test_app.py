import unittest
from news_app import create_app
from flask import request


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_filename='test_settings.py')

    def test_request_args(self):
        with self.app.test_request_context('/?name=Douglas'):
            self.assertEqual(request.args.get('name'), 'Douglas')
