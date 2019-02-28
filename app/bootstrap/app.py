# -*- coding: utf-8 -*-
from fibonacci.application.framewoork import FalconApi


class App:
    """Class App Base"""

    def __init__(self):
        self.api = FalconApi().api
