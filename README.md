## Problem:
Finding the shortest path from a given source node to a target node in a graph.
The data base i use is Israel roads in db/israel.csv from: [openstreetmap](https://www.openstreetmap.org/#map=19/32.08519/34.78910)

## Algorithms:
* best first search
* UCS
* A star
* idA star

### best first search:
Uses a priority queue (util/priority_queue.py) with a heuristic function.
The algorithm starts from the source node and add all his children to the priority queue, then dequeue the node with the minimum heuristic value, and expands it until the target node is reached.

### UCS:
The UCS algorithm is an optimal algorithm.
<br>
Calling best first search with heuristic function that calculate the travel time from thee source to th current node.

### A star:
The A star algorithm is an optimal algorithm.
<br>
Calling best first search with heuristic function that calculate the sum of travel time from the source to the current node and evaluate travel time from current node to the target.

### idA star:
The idA star algorithm is an optimal algorithm.
Iterate A star with a limit on the heuristic function from the source node, in each iteration update the limit.

