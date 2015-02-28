from collections import defaultdict
from heapq import *

bukovel_graph = [
    [0, 4,  8,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [2, 0,  2,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0, 4,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0, 0,  0,  0,  6,  0,  4,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0],
    [0, 0,  0,  3,  0,  0,  0,  0,  0,  4,  3,  0,  0,  0,  0,  0,  0,  0],
    [0, 0,  0,  0,  0,  0,  0,  16, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0, 0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0, 0,  0,  0,  0,  8,  0,  0,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0],
    [0, 0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  8,  0,  0,  0],
    [0, 0,  0,  0,  8,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0, 0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  4,  0,  0,  0],
    [0, 0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0],
    [0, 0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  3,  0,  6,  0,  6,  0,  0],
    [0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  6,  0,  0,  4,  0,  10, 0],
    [0, 0,  0,  0,  0,  0,  0,  0,  16, 0,  2,  0,  0,  8,  0,  0,  0,  0],
    [0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  3,  0],
    [0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  3],
    [0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  6,  0]
]


def route_from(start_point):
    end_point = 6
    g = defaultdict(list)

    for row_idx, row in enumerate(bukovel_graph):
        for elem_idx, elem in enumerate(row):
            if elem != 0:
                g[row_idx].append((elem, elem_idx))
    q, seen = [(0, start_point, ())], set()

    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = [x for x in path]
            path.append(v1)
            if v1 == end_point:
                return {'time': cost, 'checkpoints': path}

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))
