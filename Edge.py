class Edge:
    def __init__(self, id, source, target, weight=None):
        self.id = id
        self.node0 = source
        self.node1 = target
        self.weight = int(weight)  
        
    def __str__(self):
        if self.weight is not None:
            return f"{self.id} ({self.node0.id} -- {self.node1.id}, Weight: {self.weight})"
        else:
            return f"{self.id} ({self.node0.id} -- {self.node1.id})"


