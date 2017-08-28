import unittest
from news_app import create_app
from flask import request


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    def test_request_args(self):
        with self.app.test_request_context('/?name=Douglas'):
            self.assertEqual(request.args.get('name'), 'Douglas')
