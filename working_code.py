import sys
import itertools as it
import numpy as np

if __name__ == "__main__":
    Max_Length = 4
    graph = np.array([
        [0, 3, np.inf, 8],
        [8, 0, 2, np.inf],
        [5, np.inf, 0, 1],
        [2, np.inf, np.inf, 0]
    ])

def floyd_algorithm(graph):
    num_nodes = len(graph)
    distance = np.copy(graph)

    for intermediate in range(num_nodes):
        for start_node in range(num_nodes):
            for end_node in range(num_nodes):
                if start_node == end_node:
                    continue
                distance[start_node][end_node] = min(distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node])

    return distance

shortest_distances = floyd_algorithm(graph)
print("Shortest distance:")
print(shortest_distances)