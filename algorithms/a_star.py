from algorithms.best_first_search import best_first_search
from ways import load_map_from_csv, compute_distance
from ways.info import SPEED_RANGES, ROAD_TYPES


def heuristic_function(lat1, lon1, lat2, lon2):
    max_speed = max([SPEED_RANGES[highway_type][1] for highway_type in range(len(ROAD_TYPES))])
    return compute_distance(lat1, lon1, lat2, lon2) / max_speed


def a_star(roads, source, target):
    def g(node):
        return node.cost

    def h(node):
        return heuristic_function(node.lat, node.lon, roads[target].lat, roads[target].lon)

    def f(node):
        return g(node) + h(node)

    path, time = best_first_search(roads, source, target, f)
    return path, time, h(roads[source])
