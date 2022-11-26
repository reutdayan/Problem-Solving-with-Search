from algorithms.best_first_search import best_first_search
from ways import load_map_from_csv


def ucs(roads, source, target):
    def g(node):
        return node.cost

    return best_first_search(roads, source, target, g)
