import random
from Node import Node
from Edge import Edge
import numpy as np
import pygame


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
        if node_id not in forest:    return node_id
        else:    return self.find_root(forest[node_id], forest)

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

    def spring_layout(self, c1=2, c2=1, c3=1, c4=0.1):
    #           Spring Layout Algorithm
    #   Adjusts the positions of nodes in a graph based on attractive 
    #   and repulsive forces, to create an aesthetically pleasing layout.
        """
            def spring_layout(self, c1=1, c2=1, c3=1, c4=0.001):
                :self: The graph
                :c1: Attraction force constant for neighboring nodes
                :c2: Distance normalization constant for attraction force
                :c3: Repulsion force constant for non-adjacent nodes
                :c4: Constant factor for node movement
        """
        for node in self.nodes.values():
            forces = np.array([0.0, 0.0])

            # Force of attraction between neighboring nodes 
            for neighbor in node.neighbors:
                delta = neighbor.position - node.position
                distance = max(np.linalg.norm(delta), 0.1)
                force_attraction = c1 * np.log(distance / c2)
                forces += force_attraction * delta / (distance + 0.1)
                
            # Repulsion force between non-adjacent nodes 
            for other_node in self.nodes.values():
                if other_node != node:
                    delta = other_node.position - node.position
                    distance = max(np.linalg.norm(delta), 0.1)
                    force_repulsion = c3 / np.sqrt(distance)
                    forces -= force_repulsion * delta / (distance + 0.1)

            node.position += c4 * forces

    def visualize(self, screen, width=800, height=600, node_radius=5):
        # Maximum and minimum positions
        max_x, max_y = np.max([node.position for node in self.nodes.values()], axis=0)
        min_x, min_y = np.min([node.position for node in self.nodes.values()], axis=0)

        # Calculate the scale factor
        scale_factor = min(width / (max_x - min_x), height / (max_y - min_y))

        for node in self.nodes.values():
            # Apply scale factor and adjust to visual range
            scaled_position = (node.position - np.array([min_x, min_y])) * scale_factor
            scaled_position = np.clip(scaled_position, a_min=0, a_max=(width, height))

            # Draw the scaled nodes
            pygame.draw.circle(screen, (0, 0, 255), (int(scaled_position[0]), int(scaled_position[1])), node_radius)

        for edge in self.edges.values():
            n0 = edge.node0.position
            n1 = edge.node1.position

            # Apply scale factor and adjust to visual range
            scaled_n0 = (n0 - np.array([min_x, min_y])) * scale_factor
            scaled_n1 = (n1 - np.array([min_x, min_y])) * scale_factor
            scaled_n0 = np.clip(scaled_n0, a_min=0, a_max=(width, height))
            scaled_n1 = np.clip(scaled_n1, a_min=0, a_max=(width, height))

            # Draw the scaled edges
            pygame.draw.line(screen, (0, 0, 0), (int(scaled_n0[0]), int(scaled_n0[1])),
                            (int(scaled_n1[0]), int(scaled_n1[1])), 1)


