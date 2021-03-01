from math import sqrt
import itertools
import sys


def calculate_distance(p1, p2):
    return sqrt((int(p2[0]) - int(p1[0])) ** 2 + (int(p2[1]) - int(p1[1])) ** 2)


def generate_distance_matrix(coordinates):
    matrix = []
    for a in coordinates:
        row = []
        for b in coordinates:
            row.append(calculate_distance(a, b))
        matrix.append(row)
    return matrix


class MST:
    def __init__(self, vertices_len):
        self.V = vertices_len
        self.graph = [[0] * vertices_len] * vertices_len

    def returnMST(self, parent):
        MST = []
        for i in range(1, self.V):
            edge = (parent[i], i, self.graph[i][parent[i]])
            MST.append(edge)
        return MST

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def prim_MST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and mstSet[v] == False
                    and key[v] > self.graph[u][v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u
        return self.returnMST(parent)


def _odd_vertices_of_MST(M, number_of_nodes):
    """
    Returns the vertices having Odd degree in the Minimum Spanning Tree(MST).
    """
    odd_vertices = [0 for i in range(number_of_nodes)]
    for u, v, _ in M:
        odd_vertices[u] = odd_vertices[u] + 1
        odd_vertices[v] = odd_vertices[v] + 1
    odd_vertices = [
        vertex for vertex, degree in enumerate(odd_vertices) if degree % 2 == 1
    ]
    return odd_vertices


def bipartite_graph(M, bipartite_set, odd_vertices):
    bipartite_graphs = []
    vertex_sets = []
    for vertex_set1 in bipartite_set:
        vertex_set1 = list(sorted(vertex_set1))
        vertex_set2 = []
        for vertex in odd_vertices:
            if vertex not in vertex_set1:
                vertex_set2.append(vertex)
        matrix = [
            [-1000000 for j in range(len(vertex_set2))] for i in range(len(vertex_set1))
        ]
        for i in range(len(vertex_set1)):
            for j in range(len(vertex_set2)):
                if vertex_set1[i] < vertex_set2[j]:
                    matrix[i][j] = M[vertex_set1[i]][vertex_set2[j]]
                else:
                    matrix[i][j] = M[vertex_set2[j]][vertex_set1[i]]
        bipartite_graphs.append(matrix)
        vertex_sets.append([vertex_set1, vertex_set2])
    return [bipartite_graphs, vertex_sets]


if __name__ == "__main__":
    array = [
        (0, 200, 800),
        (1, 3600, 2300),
        (2, 3100, 3300),
        (3, 4700, 5750),
        (4, 5400, 5750),
        (5, 5608, 7103),
        (6, 4493, 7102),
        (7, 3600, 6950),
        (8, 3100, 7250),
        (9, 4700, 8450),
        (10, 5400, 8450),
        (11, 5610, 10053),
        (12, 4492, 10052),
        (13, 3600, 10800),
        (14, 3100, 10950),
        (15, 4700, 11650),
        (16, 5400, 11650),
        (17, 6650, 10800),
        (18, 7300, 10950),
        (19, 7300, 7250),
        (20, 6650, 6950),
    ]
    mst = MST(len(array))
    mst.graph = generate_distance_matrix(array)
    triples = mst.prim_MST()
    odd_vertices = _odd_vertices_of_MST(triples, len(array))
    bipartite_set = [
        set(i)
        for i in itertools.combinations(set(odd_vertices), int(len(odd_vertices) / 2))
    ]
    bipartite_graphs = bipartite_graph(mst.graph, bipartite_set, odd_vertices)
    print(bipartite_graphs)
