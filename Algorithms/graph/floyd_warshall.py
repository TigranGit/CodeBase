from pprint import pprint

INF = float("inf")


class Floyd_Warshall:
    graph = None
    graph_len = None

    def __init__(self, graph):
        self.graph = graph
        self.graph_len = len(graph)

    def solve(self):
        for k in range(self.graph_len):
            for i in range(self.graph_len):
                for j in range(self.graph_len):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        return self.graph


if __name__ == "__main__":
    # fmt: off
    graph = [
        [ 0,   5,  INF,  10],
        [INF,  0,   3,  INF],
        [INF, INF,  0,   1 ],
        [INF, INF, INF,  0 ]
    ]
    # fmt: on

    solver = Floyd_Warshall(graph)
    pprint(solver.solve(), width=60)
