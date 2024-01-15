import random
from Node import Node
from Edge import Edge


class Graph:

    def __init__(self, digraph=False, autocycle=False):
        self.id = 'Grafo'
        self.digraph = digraph
        self.autocycle = autocycle
        self.nodes = {}
        self.edges = {}
        
    def add_node(self, name, distance=float('inf')):
        node = self.nodes.get(name)

        if node is None:
            node = Node(name)
            node.distance = distance 
            self.nodes[name] = node

        return node


    def add_edge(self, name, node0, node1, weight=None): 
            edge = self.edges.get(name)

            if edge is None:
                n0 = self.add_node(node0)
                n1 = self.add_node(node1)
                edge = Edge(name, n0, n1, weight)

                self.edges[name] = edge

                n0.neighbors.append(n1)
                n1.neighbors.append(n0)

                n0.edges.append(edge)
                n1.edges.append(edge)

            return edge

    def get_edge(self, node_id_0, node_id_1):
        for edge in self.edges.values():
            if (edge.node0.id == node_id_0 and edge.node1.id == node_id_1) or \
            (edge.node0.id == node_id_1 and edge.node1.id == node_id_0):
                return edge
        return None

    def get_node(self, name):
        return self.nodes.get(name)

    def get_degree(self, node_name):
        n = self.get_node(node_name)
        if n is None:
            return 0
        
        return len(n.neighbors)
    
    def get_random_edge(self):
        return random.choice(list[self.edges.values()])
    
    def find_root(self, node_id, forest):
        if node_id not in forest:
            return node_id
        else:
            return self.find_root(forest[node_id], forest)

    def save_graph(self, filename):
        try:
            value = 'digraph X {\n' if self.digraph else 'graph X {\n'

            for node in self.nodes.values():
                if hasattr(node, 'distance'):
                    distance_label = f' ({node.distance})' if node.distance != float('inf') else '' 
                    value += f' {node.id} [label="nodo{node.id}{distance_label}"];\n'

            for edge in self.edges.values():
                n0 = edge.node0.id
                n1 = edge.node1.id
                weight_label = f' [label="{edge.weight}"]' if edge.weight is not None else ''  # Weight label
                weight = f' [weight={edge.weight}]' if edge.weight is not None else ''  # Weight
                char = ' -> ' if self.digraph else ' -- '


                value += f'  {n0}{char}{n1} {weight_label};\n'

            value += '}\n'

            with open(filename, "w") as file:
                file.write(value)
            
            print(f"Se ha generado el archivo DOT: {filename}")
        except Exception as e:
            print(f"Error al escribir el archivo DOT: {e}")



