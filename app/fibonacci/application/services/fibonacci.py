from fibonacci.application.request.fibonacci import FibonacciSuccessionRequest
from fibonacci.domain.services.fibonacci import FibonacciSuccessionDomainService


class FibonacciSuccessionService(object):

    def __init__(self):
        self.__domain_service = FibonacciSuccessionDomainService()

    def execute(self, request: FibonacciSuccessionRequest):
        return self.__domain_service.get_fibonacci_element_by_number(request.number())
