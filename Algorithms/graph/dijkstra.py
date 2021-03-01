from collections import defaultdict


class Dijkstra:
    graph = None

    def __init__(self, edge_list, directed=False):
        self.edge_list = edge_list
        self.directed = directed

    def build_graph(self):
        self.graph = defaultdict(list)
        seen_edges = defaultdict(int)
        for src, dst, weight in self.edge_list:
            seen_edges[(src, dst, weight)] += 1
            if (
                seen_edges[(src, dst, weight)] > 1
            ):  # checking for duplicated edge entries
                continue
            self.graph[src].append((dst, weight))
            if not self.directed:
                self.graph[dst].append((src, weight))

    def dijkstra(self, src, dst=None):
        nodes = []
        for n in self.graph:
            nodes.append(n)
            nodes += [x[0] for x in self.graph[n]]

        q = set(nodes)
        nodes = list(q)
        dist = dict()
        prev = dict()
        for n in nodes:
            dist[n] = float("inf")
            prev[n] = None

        dist[src] = 0
        while q:
            u = min(q, key=dist.get)
            q.remove(u)
            if dst is not None and u == dst:
                return dist[dst], prev
            for v, w in self.graph.get(u, ()):
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        return dist, prev

    def find_path(self, pr, node):
        """ generate path list based on parent points 'prev' """
        p = []
        while node is not None:
            p.append(node)
            node = pr[node]
        return p[::-1]


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

    dijkstra = Dijkstra(edges)
    dijkstra.build_graph()

    print("--- Single source, single destination ---")
    d, prev = dijkstra.dijkstra("A", "E")
    path = dijkstra.find_path(prev, "E")
    print(f"A -> E: distance = {d}, path = {path}")

    d, prev = dijkstra.dijkstra("F", "G")
    path = dijkstra.find_path(prev, "G")
    print(f"F -> G: distance = {d}, path = {path}")

    print("--- Single source, all destinations ---")
    ds, prev = dijkstra.dijkstra("A")
    for k in ds:
        path = dijkstra.find_path(prev, k)
        print(f"A -> {k}: distance = {ds[k]}, path = {path}")
