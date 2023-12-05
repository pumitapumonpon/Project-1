import random
import math
from Graph import Graph
from collections import deque
import numpy
import Node



def grid_model(m, n, digraph = False):
    # Grid model G_{m,n} (Modelo de malla). 
    # Creates m*n nodes. To the node n_{i,j} creates an edege with the node n_{i+1, j} 
    # and another edge with the node n_{i,j+1}, for i < m and j < n.
    """     Generates grid graph
        def grafoMalla(m, n, digraph=False): 
            :m: columns number (> 1)
            :n: rows number (> 1)
            :digraph: it's a digraph?
            :return: graph generated
    """
    graph = Graph(digraph)

    for i in range(m):
        for j in range(n):
            actual_node = f'{i}-{j}'
           
            node = graph.add_node(actual_node)
            node.position = numpy.array([i, j]) 

            if i < m - 1:
                right_node = f'{i + 1}-{j}'
                graph.add_edge(f'Arista {actual_node}--{right_node}', actual_node, right_node)

            if j < n - 1:
                under_node = f"{i}-{j + 1}"
                graph.add_edge(f'Arista {actual_node}--{under_node}', actual_node, under_node)

    return graph

    
def erdos_renyi_model(n, m, digraph=False, autocycle=False):
    #   Erdös and Rényi Model G(n,m).
    #   Creates n edges and choose uniformly at random m
    #   diferents pairs of diferent edges.
    """     Generates a random graph by Erdos-Renyi model.
      def grafoErdosRenyi(n, m, digraph=False, auto=False):
        :n: nodes number (> 0)
        :m: edges number (>= n-1)
        :digraph: it's a digraph?
        :auto-cycles: allows auto-cycles?
        :return: graph generated
    """
    if n <= 0 or m < n - 1:
        raise ValueError("Valores incorrectos para n y m")
        #n = 1, m =  n-1

    graph = Graph(digraph, autocycle)
    
    for i in range(n):
        graph.add_node(str(i))

    while len(graph.edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)

        if u != v: 
            graph.add_edge(f'Arista {u}--{v}', u, v)

    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if i != j:
    #             graph.add_edge(f'Arista {i}--{j}', i, j)

    return graph

 
def gilbert_model(n, p, digraph=False, autocycle=False):
    #   Gilbert Model G(n,p).
    # Creates m edges, creates n vertices, and put an edge between 
    # each independent and uniform pair with probability p.
    """     Generate random graph by Gilbert model.
        def grafoGilbert(n, p, dirigido=False, auto=False):
            :n: nodes number (> 0)
            :p: probability to create an edge (0, 1)
            :digraph:  it's a digraph?
            :auto-cycles: allows auto-cycles?
            :return: graph generated
    """
    if n <= 0 or p < 0 or p > 1:
        raise ValueError("Valores incorrectos para n o p")

    graph = Graph(digraph, autocycle)

    nodes = [str(i) for i in range(n)]
    for node in nodes:
         graph.add_node(node)

    for n1 in nodes:
        for n2 in nodes:
            if n1 != n2 and (autocycle or n1 != n2) and random.random() < p:
                graph.add_edge(f"Arista{n1}--{n2}", n1, n2)
    
    return graph


def euclidean_distance(node0, node1):
        return math.sqrt((node0.position[0] - node1.position[0]) ** 2 + (node0.position[1] - node1.position[1]) ** 2)

def geographic_model(n, r, digraph=False, autocycle=False):
    #   Simple Geographic Model G_{n,r}.
    # Place n nodes in a unit rectangle with uniform (or normal) coordinates 
    # and place an edge between each pair that remains at distance r or less.
    """     Generate an random graph by Simple Geographic Model 
      def grafoGeografico(n, r, dirigido=False, auto=False):
        :n: nodes number (> 0)
        :r: maximum distance to create a node (0, 1)
        :digraph: it's a digraph?
        :auto-cycles:  allows auto-cycles?
        :return: graph generated
    """
    if n <= 0 or r < 0 or r > 1:
        raise ValueError("Valores incorrectos para n o r")

    graph = Graph(digraph, autocycle)

    for i in range(n):
        node = graph.add_node(str(i))
        node.position[0] = random.random()
        node.position[1] = random.random()

    print(len(graph.nodes))
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = euclidean_distance(graph.get_node(str(i)), (graph.get_node(str(j))))
                if distance <= r*r:
                    graph.add_edge(f"Arista {str(i)}--{str(j)}", i, j)
    print(len(graph.nodes))
    return graph

 
def random_array(n):
    if n > 1:   return random.sample(range(n), n)
    else:       return [0]
  
def barabasi_albert_model(n, d, digraph=False, autocycle=False):
    #       Variant of the Barabási-Albert Model G_{n,d}. 
    # Place n nodes one by one, assigning each d edges to different vertices 
    # such that the probability that the new vertex connects to an existing vertex v is proportional 
    # to the number of edges v currently has - the first d vertices everyone connects to everyone.
    """     Generates random graph by Barabasi-Albert Model
        def grafoBarabasiAlbert(n, d, dirigido=False, auto=False):
            :n: nodes number (> 0)
            :d: grado máximo esperado por cada nodo (> 1)
            :digraph: it's a digraph?
            :auto-cycles: allows auto-cycles?
            :return: generated graph
    """
    if n <= 0 or d <= 1:
        raise ValueError("Valores incorrectos para n o d")

    graph = Graph(digraph, autocycle)
    
    graph.add_node(str(0))

    for u in range(1, n):
        random_nodes = random_array(u)
        for v in range(u):
            degree = graph.get_degree(str(random_nodes[v]))
            p = 1 - degree / d
            if random.random() < p:
                graph.add_edge(f"Arista {u}--{str(random_nodes[v])}", u, str(random_nodes[v]))

    return graph


def dorogovtsev_mendes_model(n, digraph=False):
    #           Gn Dorogovtsev-Mendes Model. 
    #   Creates 3 nodes and 3 edges forming a triangle. 
    #   Then, for each additional node, select 
    #   a random edge and edges are created between the
    #   new node and the ends of the selected edge. j,
    """     Generates a random graph by Dorogovtsev-Mendes Model 
        def grafoDorogovtsevMendes(n, dirigido=False):
            :n: node number (≥ 3)
            :digraph: it's a digraph?
            :return: graph generated
    """
    if n < 3:
        n = 3

    graph = Graph(digraph)

    for i in range(3):
        graph.add_node(str(i))
    graph.add_edge("Arista 0--1", 0, 1)
    graph.add_edge("Arista 1--2", 1, 2)
    graph.add_edge("Arista 2--0", 2, 0)

    for i in range(3, n):
        graph.add_node(str(i))
        edges = list(graph.edges.values())

        selected_edge = random.choice(edges)

        graph.add_edge(f"Arista {i}--{selected_edge.node0}", i, selected_edge.node0)
        graph.add_edge(f"Arista {i}--{selected_edge.node1}", i, selected_edge.node1)
    
    return graph



def generate_random_graph(num_nodes, probability=0.3, digraph=False, autocycle=False, weighted=False, min_weight=1, max_weight=30):
    graph = Graph(digraph=digraph, autocycle=autocycle)
    
    for node in range(num_nodes):
        graph.add_node(str(node))

    for node in range(num_nodes):
        for neighbor in range(node + 1, num_nodes):
            if random.random() < probability:
                if weighted:
                    weight = random.randint(min_weight, max_weight)
                    edge_name = f"Arista {node}--{neighbor}"
                    graph.add_edge(edge_name, str(node), str(neighbor), weight)
                else:
                    edge_name = f"Arista {node}--{neighbor}"
                    graph.add_edge(edge_name, str(node), str(neighbor))

    return graph



def BFS(graph, source_node):
    #           Breadth-First Search.
    # Consists of exploring from the source node 'start_node' 
    # and outwards in all possible directions, adding nodes one "layer" at a time.
    """     Generates a tree using Breadth-First Search 
        def BFS(graph, start_node):
            :graph: original graph
            :start_node: source node
            :return: tree BFS generated
    """
    result = Graph(digraph=graph.digraph, autocycle=graph.autocycle)

    visited = set()
    stack = deque()

    result.add_node(source_node)

    stack.append(source_node)
    visited.add(source_node.id)

    while stack:
        current_node = stack.popleft()

        node = graph.get_node(current_node.id)
        if node:
            for neighbor in node.neighbors:           
                if neighbor.id not in  visited:
                    result.add_edge(f"Arista {node.id}--{neighbor.id}", node, neighbor)
            
                    visited.add(neighbor.id)
                    stack.append(neighbor)
    return result


def DFS_R(graph, source_node, visited=set(), result=None): 
    #       Recursive Depth-First Search
    #   Consists of expanding each and every one 
    #   of the nodes that it locates, recurrently, 
    #   on a specific path and in a recursive way.
    """     Generates a tree using Recursive Depth-First Search
        def DFS_R(graph, start_node, visited=None, result=None):
            :graph: original graph
            :start_node: source node
            :visited: indicates if the current node was visited
            :result: the auxiliar graph to return the tree DFS generated
            :return: tree DFS generated
    """

    if visited is None:
        visited = set()

    if result is None:
        result = Graph(digraph=graph.digraph, autocycle=graph.autocycle)
    
    
    visited.add(source_node.id)
    result.add_node(source_node.id)

    for edge in source_node.edges: 
        if edge.node0.id == source_node.id:
            neighbor = edge.node1
        else:
            neighbor = edge.node0
        
        if neighbor.id  not in visited:
            result.add_edge(f"Arista {source_node.id}--{neighbor.id}", source_node.id, neighbor.id)
            
            result = DFS_R(graph, neighbor, visited, result)
    
    return result

                       
def DFS_I(graph, source_node):
    #       Iterative Depth-First Search 
    #   Consists of expanding each and every one 
    #   of the nodes that it locates, recurrently, 
    #   on a specific path and in a iterative way.
    """     Generates a tree using Recursive Depth-First Search
        def DFS_I(graph, start_node, visited=None, result=None):
            :graph: original graph
            :start_node: source node
            :return: tree DFS generated
    """
    result = Graph(digraph=graph.digraph, autocycle=graph.autocycle)
    visited = set()
    stack = []
    
    result.add_node(source_node)
    
    stack.append(source_node)
    visited.add(source_node.id)

    while stack:
        current_node = stack.pop()
        visited.add(current_node.id)
        
        for edge in current_node.edges:
            if edge.node0.id == source_node.id:
                neighbor = edge.node1
            else:
                neighbor = edge.node0

            if neighbor.id  not in visited:
                result.add_node(neighbor)
                result.add_edge(f"Arista {current_node.id}--{neighbor.id}", current_node, neighbor)

                visited.add(neighbor.id)
                stack.append(neighbor)

    return result



def dijkstra(self, source_node):
    start_node = self.get_node(source_node.id)

    if start_node is None:
        print(f"El nodo {source_node} no existe en el grafo.")
        return None

    start_node.distance = 0
    unvisited_nodes = list(self.nodes.values())
    result = Graph(digraph=False, autocycle=False)

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda x: x.distance)

        for edge in current_node.edges:
            if edge.node0.id == source_node.id:
                neighbor = edge.node1
            else:
                neighbor = edge.node0
            
            new_distance = current_node.distance + edge.weight

            if new_distance < neighbor.distance and not neighbor.visited: 

                result.add_node(self.get_node(current_node.id))
                result.add_node(self.get_node(neighbor.id))
                result.add_edge(f"Arista {current_node.id}--{neighbor.id}", current_node, neighbor, edge.weight)

                neighbor.visited = True
                neighbor.distance = new_distance

        current_node.visited = True
        unvisited_nodes.remove(current_node)

    return result



