class FibonacciSuccessionDomainService(object):

    def __init__(self):
        pass

    def get_fibonacci_element_by_number(self, number):
        return self.fibonacci_algorithm(int(number))

    def fibonacci_algorithm(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci_algorithm(n - 1) + self.fibonacci_algorithm(n - 2)
