class Vertex:

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def getKey(self):
        return self.vertex

    def getWeight(self):
        return self.weight

    def setWeight(self, w):
        self.weight = w

class Edge:

    def __init__(self, vertexA, vertexB, weight):
        self.edge = [vertexA, vertexB]
        self.weight = weight

    def setWeight(self, w):
        self.weight = w

    def getVertex(self):
        return self.edge


class Graph:

    def __init__(self, listOfVertex, listOfEdges):
        self.listOfEdges = listOfEdges
        self.listOfVertex = listOfVertex

    def setVertex(self, key, weight):
        v = Vertex(key, weight)
        self.listOfVertex.append(v)

    def getVertex(self):
        return self.listOfVertex

    def getEdges(self):
        return self.listOfEdges
    def printGraph(self):
        print("Vertices")
        for v in self.listOfVertex:
            print(v.vertex)
        print("Edges")
        for e in self.listOfEdges:
            print(e.edge, e.weight)
