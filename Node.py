import random
import numpy

class Node:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.neighbors = []
        self.position = numpy.array([random.random(),random.random()])

    def __str__(self):
        return f'{self.id}'


