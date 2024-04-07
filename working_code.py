def floyd_warshall_recursive(graph, k, i, j):
    if k == 0:
        return graph[i][j]

    # Calculate the distance through vertex k
    dist_via_k = floyd_warshall_recursive(graph, k - 1, i, k) + floyd_warshall_recursive(graph, k - 1, k, j)

    # Choose the minimum distance
    return min(floyd_warshall_recursive(graph, k - 1, i, j), dist_via_k)


# Example usage
if __name__ == "__main__":
    # Example graph (replace with your own)
    graph = [
        [0, 3, float("inf"), 7],
        [8, 0, 2, float("inf")],
        [5, float("inf"), 0, 1],
        [2, float("inf"), float("inf"), 0]
    ]

    n = len(graph)
    for i in range(n):
        for j in range(n):
            print(f"Shortest path from vertex {i} to {j}: {floyd_warshall_recursive(graph, n - 1, i, j)}")