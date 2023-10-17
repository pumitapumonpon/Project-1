import Algorithms as a

if __name__ == "__main__":
    #size = [30,100,500]
 
    # Generates grid graph
    grid_graph = a.grid_model(20, 25)
    grid_graph.save_graph(f"Graphs/Grid/grid_graph ({500} nodes).dot")

    # Generates Erdos-Renyi graph
    erdos_renyi_graph = a.erdos_renyi_model(500, 3500) #100 . 2000 aristas
    erdos_renyi_graph.save_graph(f"Graphs/Erdös and Rényi/erdos_renyi_graph ({500} nodes).dot")

    # Generates Gilbert graph
    gilbert_graph = a.gilbert_model(500, 0.1)
    gilbert_graph.save_graph(f"Graphs/Gilbert/gilbert_graph ({500} nodes).dot")

    # Generates Geographic graph
    geographic_graph = a.geographic_model(500, 0.35)
    geographic_graph.save_graph(f"Graphs/Geographic/geographic_graph ({500} nodes).dot")

    # Generates Barabási-Albert graph
    barabasi_albert_graph = a.barabasi_albert_model(500,25)
    barabasi_albert_graph.save_graph(f"Graphs/Barabási-Albert/barabasi_albert_graph ({500} nodes).dot")

    # Generates Dorogovtsev-Mendes graph
    dorogovtsev_mendes_graph = a.dorogovtsev_mendes_model(500)
    dorogovtsev_mendes_graph.save_graph(f"Graphs/Dorogovtsev-Mendes/dorogovtsev_mendes_graph ({500} nodes).dot")


