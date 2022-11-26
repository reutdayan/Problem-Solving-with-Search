from ways.info import SPEED_RANGES


class Node:
    def __init__(self, value, lat, lon, parent=None, cost=0):
        self.value = value
        self.lat = lat
        self.lon = lon
        self.cost = cost
        self.parent = parent

    def expand(self, roads):
        return [Node(cost=self.cost + (link.distance / 1000) / SPEED_RANGES[link.highway_type][1], parent=self,
                     value=link.target, lat=roads[link.target].lat, lon=roads[link.target].lon) for link in
                roads[self.value].links]

    def has_parent(self):
        if self.parent == None:
            return False
        return True

    def set_parent(self, parent):
        self.parent = parent

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node.value)
            node = node.parent
        return list(reversed(path_back))

    def __lt__(self, node):
        return self.value < node.value

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.value)
