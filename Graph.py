import random
from Node import Node
from Edge import Edge


class Graph:

    def __init__(self, digraph, autocycle=True):
        self.id = 'Grafo'
        self.digraph = digraph
        self.autocycle = autocycle
        self.nodes = {}
        self.edges = {}
        
    def add_node(self, name):
        node = self.nodes.get(name)

        if node is None:
            node = Node(name)
            self.nodes[name] = node
        
        return node

    def add_edge(self, name, node0, node1):
        edge = self.edges.get(name)

        if edge is None:
            n0 = self.add_node(node0)
            n1 = self.add_node(node1)
            edge = Edge(name, n0, n1)

            self.edges[name] = edge


            n0.neighbors.append(n1)
            n1.neighbors.append(n0)

            n0.edges.append(edge)
            n1.edges.append(edge)

        return edge
    
    def has_edge(self, node_u, node_v):
    # """
    # Verifica si existe una arista entre los nodos node_u y node_v en el grafo.
    # :param node_u: Nombre del primer nodo.
    # :param node_v: Nombre del segundo nodo.
    # :return: True si hay una arista entre los nodos, False en caso contrario.
    # """
        if node_u in self.nodes:
            # Obtiene la lista de vecinos del nodo node_u.
            neighbors_u = self.nodes[node_u].neighbors
            # Verifica si el nodo node_v está en la lista de vecinos de node_u.
            if node_v in neighbors_u:
                return True
        # Si no se encuentra una arista entre los nodos, se retorna False.
        return False

    def get_node(self, name):
        return self.nodes.get(name)

    def get_degree(self, node_name):
        n = self.get_node(node_name)
        if n is None:
            return 0
        
        return len(n.neighbors)
    
    def get_random_edge(self):
        return random.choice(list[self.edges.values()])
    
    def save_graph(self, filename):
        value = 'digraph X {\n' if self.digraph else 'graph X {\n'
        for e in self.edges.values():
            n0 = e.node0.id
            n1 = e.node1.id
            char = ' -> ' if self.digraph else ' -- '
            value += str(n0) + char + str(n1) + ';\n' 
        value += '}\n'

        with open(filename, "w") as file:
            file.write(value)
    

