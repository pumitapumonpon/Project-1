import Algorithms as a
import random
import sys
import pygame
sys.setrecursionlimit(10000)



if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    size = 500

    # Initialize Pygame
    pygame.init()
    width, height = 1200, 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Spring Algorithm Visualization")
    clock = pygame.time.Clock()

    graph = a.grid_model(25,20)
    graph = a.erdos_renyi_model(size, 1020)
    graph = a.gilbert_model(size, 0.1)
    graph = a.geographic_model(size, 0.35)
    graph = a.barabasi_albert_model(size, 7)
    graph = a.dorogovtsev_mendes_model(size)
    
    #Pygame
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        graph.spring_layout()
        graph.visualize(screen, width, height)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

    # Note: The optimization of this part of the code is pending.
    #========= Generates grid graph ============
    # graph = a.grid_model(10,50) 
    # a.add_random_weights(graph, 1, 20)
    # graph.save_graph(f"Graphs/BFS/grid_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/DFS/grid_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Kruskal/grid_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Prim/grid_graph ({size} nodes).dot")

    # source_node = graph.get_node(random.choice(list(graph.nodes.keys())))
    # graph = a.BFS(graph, source_node)
    # graph.save_graph(f"Graphs/BFS/grid_bfs ({size} nodes).dot")

    # graph = a.DFS_I(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/grid_dfsI ({size} nodes).dot")

    # graph = a.DFS_R(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/grid_dfsR ({size} nodes).dot")

    # graph = a.dijkstra(graph, source_node)
    # graph.save_graph(f"Graphs/Dijkstra/grid_dijkstra ({size} nodes).dot")

    # graph = a.KruskalD(graph)
    # graph.save_graph(f"Graphs/Kruskal/grid_kruskalD ({size} nodes).dot")

    # graph = a.KruskalI(graph)
    # graph.save_graph(f"Graphs/Kruskal/grid_kruskalI ({size} nodes).dot")

    # result_tree = a.Prim(graph)
    # result_tree.save_graph(f"Graphs/Prim/grid_prim ({size} nodes).dot")

    #========= Generates Erdos-Renyi graph ============
    # graph = a.erdos_renyi_model(size, 290)
    # a.add_random_weights(graph, 1, 20)
    # graph.save_graph(f"Graphs/BFS/erdos_renyi_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/DFS/erdos_renyi_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Kruskal/erdos_renyi_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Prim/erdos_renyi_graph ({size} nodes).dot")

    # source_node = graph.get_node(random.choice(list(graph.nodes.keys())))
    # graph = a.BFS(graph, source_node)
    # graph.save_graph(f"Graphs/BFS/erdos_renyi_bfs ({size} nodes).dot")

    # graph = a.DFS_I(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/erdos_renyi_dfsI ({size} nodes).dot")

    # graph = a.DFS_R(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/erdos_renyi_dfsR ({size} nodes).dot")

    # graph = a.dijkstra(graph, source_node)
    # graph.save_graph(f"Graphs/Dijkstra/erdos_renyi_dijkstra ({size} nodes).dot")

    # graph = a.KruskalD(graph)
    # graph.save_graph(f"Graphs/Kruskal/erdos_renyi_kruskalD ({size} nodes).dot")

    # graph = a.KruskalI(graph)
    # graph.save_graph(f"Graphs/Kruskal/erdos_renyi_kruskalI ({size} nodes).dot")

    # result_tree = a.Prim(graph)
    # result_tree.save_graph(f"Graphs/Prim/erdos_renyi_prim ({size} nodes).dot")

    # # ========= Generates Gilbert graph ============
    # graph = a.gilbert_model(size, 0.1)
    # a.add_random_weights(graph, 1, 20)
    # graph.save_graph(f"Graphs/BFS/gilbert_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/DFS/gilbert_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Kruskal/gilbert_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Prim/gilbert_graph ({size} nodes).dot")

    # source_node = graph.get_node(random.choice(list(graph.nodes.keys())))
    # graph = a.BFS(graph, source_node)
    # graph.save_graph(f"Graphs/BFS/gilbert_bfs ({size} nodes).dot")

    # graph = a.DFS_I(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/gilbert_dfsI ({size} nodes).dot")

    # graph = a.DFS_R(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/gilbert_dfsR ({size} nodes).dot")

    # graph = a.dijkstra(graph, source_node)
    # graph.save_graph(f"Graphs/Dijkstra/gilbert_dijkstra ({size} nodes).dot")

    # graph = a.KruskalD(graph)
    # graph.save_graph(f"Graphs/Kruskal/gilbert_kruskalD ({size} nodes).dot")

    # graph = a.KruskalI(graph)
    # graph.save_graph(f"Graphs/Kruskal/gilbert_kruskalI ({size} nodes).dot")

    # result_tree = a.Prim(graph)
    # result_tree.save_graph(f"Graphs/Prim/gilbert_prim ({size} nodes).dot")


    # # ========= Generates Geographic graph ============
    # graph = a.geographic_model(size, 0.35)
    # a.add_random_weights(graph, 1, 20)
    # graph.save_graph(f"Graphs/BFS/geographic_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/DFS/geographic_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Kruskal/geographic_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Prim/geographic_graph ({size} nodes).dot")

    # source_node = graph.get_node(random.choice(list(graph.nodes.keys())))
    # graph = a.BFS(graph, source_node)
    # graph.save_graph(f"Graphs/BFS/geographic_bfs ({size} nodes).dot")

    # graph = a.DFS_I(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/geographic_dfsI ({size} nodes).dot")

    # graph = a.DFS_R(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/geographic_dfsR ({size} nodes).dot")

    # graph = a.dijkstra(graph, source_node)
    # graph.save_graph(f"Graphs/Dijkstra/geographic_dijkstra ({size} nodes).dot")

    # graph = a.KruskalD(graph)
    # graph.save_graph(f"Graphs/Kruskal/geographic_kruskalD ({size} nodes).dot")

    # graph = a.KruskalI(graph)
    # graph.save_graph(f"Graphs/Kruskal/geographic_kruskalI ({size} nodes).dot")

    # result_tree = a.Prim(graph)
    # result_tree.save_graph(f"Graphs/Prim/geographic_prim ({size} nodes).dot")

    # # ========= Generates Barabási-Albert graph ============
    # graph = a.barabasi_albert_model(size, 20)
    # a.add_random_weights(graph, 1, 20)
    # graph.save_graph(f"Graphs/BFS/barabasi_albert_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/DFS/barabasi_albert_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Kruskal/barabasi_albert_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Prim/barabasi_albert_graph ({size} nodes).dot")

    # source_node = graph.get_node(random.choice(list(graph.nodes.keys())))
    # graph = a.BFS(graph, source_node)
    # graph.save_graph(f"Graphs/BFS/barabasi_albert_bfs ({size} nodes).dot")

    # graph = a.DFS_I(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/barabasi_albert_dfsI ({size} nodes).dot")

    # graph = a.DFS_R(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/barabasi_albert_dfsR ({size} nodes).dot")
    
    # graph = a.dijkstra(graph, source_node)
    # graph.save_graph(f"Graphs/Dijkstra/barabasi_albert_dijkstra ({size} nodes).dot")

    # graph = a.KruskalD(graph)
    # graph.save_graph(f"Graphs/Kruskal/barabasi_albert_kruskalD ({size} nodes).dot")

    # graph = a.KruskalI(graph)
    # graph.save_graph(f"Graphs/Kruskal/barabasi_albert_kruskalI ({size} nodes).dot")

    # result_tree = a.Prim(graph)
    # result_tree.save_graph(f"Graphs/Prim/barabasi_albert_prim ({size} nodes).dot")

    # # ========= Dorogovtsev-Mendes graph ============
    # graph = a.dorogovtsev_mendes_model(size)
    # a.add_random_weights(graph, 1, 20)
    # graph.save_graph(f"Graphs/BFS/dorogovtsev_mendes_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/DFS/dorogovtsev_mendes_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Kruskal/dorogovtsev_mendes_graph ({size} nodes).dot")
    # graph.save_graph(f"Graphs/Prim/dorogovtsev_mendes_graph ({size} nodes).dot")

    # source_node = graph.get_node(random.choice(list(graph.nodes.keys())))
    # graph = a.BFS(graph, source_node)
    # graph.save_graph(f"Graphs/BFS/dorogovtsev_mendes_bfs ({size} nodes).dot")

    # graph = a.DFS_I(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/dorogovtsev_mendes_dfsI ({size} nodes).dot")

    # graph = a.DFS_R(graph, source_node)
    # graph.save_graph(f"Graphs/DFS/dorogovtsev_mendes_dfsR ({size} nodes).dot")
    
    # graph = a.dijkstra(graph, source_node)
    # graph.save_graph(f"Graphs/Dijkstra/dorogovtsev_mendes_dijkstra ({size} nodes).dot")

    # graph = a.KruskalD(graph)
    # graph.save_graph(f"Graphs/Kruskal/dorogovtsev_mendes_kruskalD ({size} nodes).dot")

    # graph = a.KruskalI(graph)
    # graph.save_graph(f"Graphs/Kruskal/dorogovtsev_mendes_kruskalI ({size} nodes).dot")

    # result_tree = a.Prim(graph)
    # result_tree.save_graph(f"Graphs/Prim/dorogovtsev_mendes_prim ({size} nodes).dot")

    
