# add queue stuff?
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

# add graph stuff


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("can not make edge")


def earliest_ancestor(ancestors, starting_node):
    # passing pairs of vertices (parent, child)
    # add edges to link them
    # probably do a BFS to find children
    # no ancestor = -1
    # ties = lowest numeric ID

    # call graph function to start "family"
    family = Graph()

    # data comes in pairs from ancestors, (parent, child)
    for pair in ancestors:
        # need to store the vertices in order
        family.add_vertex(pair[0])
        family.add_vertex(pair[1])
        # need to make an edge pointing backwards, up the ancestor tree
        family.add_edge(pair[1], pair[0])

    # need to store the paths of ancestry in a queue format
    AnPaths = Queue()
    AnPaths.enqueue([starting_node])
    # do a BFS from starting node to find paths
    # situation if there is no ancestor
    ancestor = -1
    # path is one if there is no ancestor
    longestPath = 1

    while AnPaths.size() > 0:
        path = AnPaths.dequeue()
        vertex = path[-1]

        if (len(path) >= longestPath and vertex < ancestor) or (len(path) > longestPath):
            ancestor = vertex
            longestPath = len(path)

        for neighbor in family.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(neighbor)
            AnPaths.enqueue(path_copy)

    return ancestor
