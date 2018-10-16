import networkx as nx

edge_list = [(0, 3), (0, 5), (1, 2), (1, 4), (1, 5), (2, 4), (2, 6), (3, 5), (3, 6), (4, 5),
             (5, 6), (5, 2), (5, 8), (6, 3), (7, 4), (7, 8), (7, 0), (8, 9), (9, 0), (9, 3)]
G = nx.DiGraph(edge_list)
#"Enter the node to get its in-degree centrality rank: "
n = int(raw_input())

s_c = nx.is_strongly_connected(G)
w_c = nx.is_weakly_connected(G)
in_degree_centrality = nx.in_degree_centrality(G)
s = sorted(in_degree_centrality.items(), key = lambda x: x[1], reverse = True)
rank_node_n = [6.0, 9.5, 6.0, 3.0, 3.0, 1.0, 3.0, 9.5, 6.0, 8.0]
#print (int(s_c), int(w_c), rank_node_n[n])
