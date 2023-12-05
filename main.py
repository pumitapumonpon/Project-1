import Algorithms as a
import random
import sys
sys.setrecursionlimit(10000)


if __name__ == "__main__":
    #size = [30,100,500]
 
    # Generates grid graph
    # grid_graph = a.grid_model(20, 25)
    # grid_graph.save_graph(f"Graphs/Grid/grid_graph ({500} nodes).dot")

    # Generates Erdos-Renyi graph
    # erdos_renyi_graph = a.erdos_renyi_model(500, 3500) #100 . 2000 aristas
    # erdos_renyi_graph.save_graph(f"Graphs/Erdös and Rényi/erdos_renyi_graph ({500} nodes).dot")

    # Generates Gilbert graph
    # gilbert_graph = a.gilbert_model(500, 0.1)
    # gilbert_graph.save_graph(f"Graphs/Gilbert/gilbert_graph ({500} nodes).dot")

    # Generates Geographic graph
    # geographic_graph = a.geographic_model(500, 0.35)
    # geographic_graph.save_graph(f"Graphs/Geographic/geographic_graph ({500} nodes).dot")

    # Generates Barabási-Albert graph
    # barabasi_albert_graph = a.barabasi_albert_model(500,25)
    # barabasi_albert_graph.save_graph(f"Graphs/Barabási-Albert/barabasi_albert_graph ({500} nodes).dot")

    # Generates Dorogovtsev-Mendes graph
    # dorogovtsev_mendes_graph = a.dorogovtsev_mendes_model(500)
    # dorogovtsev_mendes_graph.save_graph(f"Graphs/Dorogovtsev-Mendes/dorogovtsev_mendes_graph ({500} nodes).dot")

    # Breadth-First Search
    # bfs_graph = a.generate_random_graph(500, 0.1)
    # bfs_graph.save_graph(f"Graphs/BFS/bfs_graph_before ({500} nodes).dot")

    # source_node = bfs_graph.get_node(random.choice(list(bfs_graph.nodes.keys())))
    # bfs_graph = a.BFS(bfs_graph, source_node)
    # bfs_graph.save_graph(f"Graphs/BFS/bfs_graph_after ({500} nodes).dot")

    # Depth-Firsth Search Iterative
    # dfsi_graph = a.generate_random_graph(500, 0.1)
    # dfsi_graph.save_graph(f"Graphs/DFS/dfsi_graph_before ({500} nodes).dot")
    
    # source_node = dfsi_graph.get_node(random.choice(list(dfsi_graph.nodes.keys())))
    # dfsi_graph = a.DFS_I(dfsi_graph, source_node)
    # dfsi_graph.save_graph(f"Graphs/DFS/dfsi_graph_after ({500} nodes).dot")
    

    # Depth-Firsth Search Recursive
    # dfsr_graph = a.generate_random_graph(500, 0.1)
    # dfsr_graph.save_graph(f"Graphs/DFS/dfsr_graph_before ({500} nodes).dot")
    
    # source_node = dfsr_graph.get_node(random.choice(list(dfsr_graph.nodes.keys())))
    # dfsr_graph = a.DFS_R(dfsr_graph, source_node)
    # dfsr_graph.save_graph(f"Graphs/DFS/dfsr_graph_after ({500} nodes).dot")


    # Dijkstra
    dijkstra_graph = a.generate_random_graph(10, 0.7, False, False, True, 1, 30)
    dijkstra_graph.save_graph(f"Graphs/Dijkstra/dijkstra_graph_before ({10} nodes).dot")

    source_node = dijkstra_graph.get_node(random.choice(list(dijkstra_graph.nodes.keys())))
    dijkstra_graph = a.dijkstra(dijkstra_graph, source_node)
    dijkstra_graph.save_graph(f"Graphs/Dijkstra/dijkstra_graph_after ({10} nodes).dot")



