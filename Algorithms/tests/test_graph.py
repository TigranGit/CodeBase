import pytest

from ..graph.dijkstra import Dijkstra


default_edges = [
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


def test_dijkstra_single():
    dijkstra = Dijkstra(default_edges)
    dijkstra.build_graph()

    d, prev = dijkstra.dijkstra("A", "E")
    path = dijkstra.find_path(prev, "E")

    assert d == 14
    assert path == ["A", "B", "E"]


expected_result = {
    "C": (15, ["A", "B", "C"]),
    "E": (14, ["A", "B", "E"]),
    "F": (11, ["A", "D", "F"]),
    "B": (7, ["A", "B"]),
    "G": (22, ["A", "D", "F", "G"]),
    "A": (0, ["A"]),
    "D": (5, ["A", "D"]),
}


@pytest.mark.parametrize("expected_result", [expected_result])
def test_dijkstra_all(expected_result):
    dijkstra = Dijkstra(default_edges)
    dijkstra.build_graph()

    ds, prev = dijkstra.dijkstra("A")
    for k in ds:
        path = dijkstra.find_path(prev, k)
        assert ds[k] == expected_result[k][0]
        assert path == expected_result[k][1]
