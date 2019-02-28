from unittest import TestCase
from fibonacci.application.request.fibonacci import FibonacciSuccessionRequest


class TestFibonacciSuccessionRequest(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFibonacciSuccessionRequest, self).__init__(*args, **kwargs)
        self.number = 5

    def setUp(self):
        self._request = FibonacciSuccessionRequest(self.number)

    def test_request_valid(self):
        self.assertEqual(self._request.number(), self.number)
