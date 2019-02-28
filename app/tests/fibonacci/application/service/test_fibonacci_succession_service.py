from unittest import TestCase
from fibonacci.application.services.fibonacci import FibonacciSuccessionService
from fibonacci.application.request.fibonacci import FibonacciSuccessionRequest


class TestFibonacciSuccessionService(TestCase):

    def setUp(self):
        self._service = FibonacciSuccessionService()

    def test_execute_valid(self):
        fibonacci_results = {
            'number': 10,
            'result': 55
        }
        result = self._service.execute(FibonacciSuccessionRequest(fibonacci_results['number']))
        self.assertTrue(isinstance(result, int))
        self.assertEqual(result, fibonacci_results['result'])
