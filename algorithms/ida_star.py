from util.node import Node
from ways import load_map_from_csv, compute_distance
from ways.info import SPEED_RANGES, ROAD_TYPES


def DFS_contour(roads, node, target, f_limit, f):
    if f(node) > f_limit:
        return None, f(node)
    if node.value == target:
        return node.path(), f_limit
    next_f = float('inf')
    for child in node.expand(roads):
        solution, new_f = DFS_contour(roads, child, target, f_limit, f)
        if solution:
            return solution, f_limit
        next_f = min(new_f, next_f)
    return None, next_f


def ida_star(roads, source, target):
    def g(node):
        return node.cost

    def h(node):
        def heuristic_function(lat1, lon1, lat2, lon2):
            max_speed = max([SPEED_RANGES[highway_type][1] for highway_type in range(len(ROAD_TYPES))])
            return compute_distance(lat1, lon1, lat2, lon2) / max_speed

        return heuristic_function(node.lat, node.lon, roads[target].lat, roads[target].lon)

    def f(node):
        return g(node) + h(node)

    f_limit = 0
    source_node = Node(source, lat=roads[source].lat, lon=roads[source].lon)
    while True:
        solution, f_limit = DFS_contour(roads, source_node, target, f_limit, f)
        if solution:
            return solution
        if f_limit == float('inf'):
            return None

