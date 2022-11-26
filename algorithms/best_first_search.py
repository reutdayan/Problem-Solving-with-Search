from util.node import Node
from util.priority_queue import PriorityQueue


def best_first_search(roads, source, target, f):
    frontier = PriorityQueue(f)
    junc = roads[source]
    frontier.append(Node(source, junc.lat, junc.lon))
    closed = set()
    while frontier:
        node = frontier.pop()
        if node.value == target:
            return node.path(), node.cost
        closed.add(node.value)
        for child in node.expand(roads):
            if child.value not in closed and child not in frontier:
                frontier.append(child)
            elif child in frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return None, None
