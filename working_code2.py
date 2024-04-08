def floyd_warshall_recursive(graph, k, i, j):
    if k == 3:
        return graph[i][j]

    # Calculate the distance through vertex k
    dist_via_k = floyd_warshall_recursive(graph, k - 1, i, k) + floyd_warshall_recursive(graph, k - 1, k, j)

    # Choose the minimum distance
    return min(floyd_warshall_recursive(graph, k - 1, i, j), dist_via_k)


# Example usage
if __name__ == "__main__":
    # Example graph (replace with your own)
    graph = [
        [0, 3, float("inf"), 8],
        [8, 0, 2, float("inf")],
        [5, float("inf"), 0, 1],
        [2, float("inf"), float("inf"), 0]
    ]

    n = len(graph)
    shortest_distances = [[floyd_warshall_recursive(graph, n - 1, i, j) for j in range(n)] for i in range(n)]

    # Print the 2D array
    for row in shortest_distances:
        print(row)