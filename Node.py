import random
import numpy

class Node:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.neighbors = []
        self.visited = False
        self.position = numpy.array([random.random(),random.random()])
        self.distance = float('inf')

    def __str__(self):
        return f'{self.id}'


