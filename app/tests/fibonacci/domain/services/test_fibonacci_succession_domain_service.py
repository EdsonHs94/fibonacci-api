from unittest import TestCase
from fibonacci.domain.services.fibonacci import FibonacciSuccessionDomainService


class TestFibonacciSuccessionDomainService(TestCase):

    def setUp(self):
        self._service = FibonacciSuccessionDomainService()

    def test_get_fibonacci_by_number(self):
        fibonacci_results = {
            'number': 10,
            'result': 55
        }
        result = self._service.get_fibonacci_element_by_number(fibonacci_results['number'])
        self.assertTrue(isinstance(result, int))
        self.assertEqual(result, fibonacci_results['result'])