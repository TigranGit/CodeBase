import numpy as np


class Bellman_Ford:
    graph = None

    def __init__(self, edge_list):
        self.graph = edge_list
        self.graph_length = len(edge_list)

    def bellman_ford(self, src):
        graph = np.array(self.graph)
        vertices = np.unique(np.hstack((graph[:, 0], graph[:, 1]))).tolist()
        dist = {v: float("inf") for v in vertices}
        dist[src] = 0

        for _ in range(self.graph_length - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        return dist


if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11),
    ]

    bellman_ford = Bellman_Ford(edges)
    ds = bellman_ford.bellman_ford("A")
    for k in ds:
        print(f"A -> {k}: distance = {ds[k]}")
