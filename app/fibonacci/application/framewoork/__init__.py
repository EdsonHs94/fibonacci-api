import falcon
from fibonacci.application.services.fibonacci import FibonacciSuccessionService
from fibonacci.application.request.fibonacci import FibonacciSuccessionRequest


class FalconApi:
    def __init__(self):
        self.api = falcon.API()
        self.api.add_route('/', HomeHandler())
        self.api.add_route('/fibonacci/{num}', FibonacciHandler())


class HomeHandler:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'message': (
                "Para la funcionalidad principal dirigirce al servicio /fibonacci/{numero}"
            )
        }

        resp.media = quote


class FibonacciHandler:
    def on_get(self, req, resp, num):

        fibonacci_service = FibonacciSuccessionService()
        request = FibonacciSuccessionRequest(num)

        service_response = fibonacci_service.execute(request)
        """Handles GET requests"""
        quote = {
            'message': (
                "Peticion Exitosa"
            ),
            'result': service_response
        }

        resp.media = quote
