import pygame

class Vertex:

    def __init__(self, vertex, weight, x, y, highlight):
        self.vertex = vertex
        self.weight = weight
        self.sprite = pygame.image.load("templates/vertex.png")
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.x = x
        self.y = y
        self.highlight = highlight

    def getKey(self):
        return self.vertex

    def getWeight(self):
        return self.weight

    def setWeight(self, w):
        self.weight = w
    def getPos(self):
        return [self.x, self.y]

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
