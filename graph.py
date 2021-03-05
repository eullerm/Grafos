import pygame

class Vertex:

    def __init__(self, vertex, weight, x, y, highlight):
        self.vertex = vertex
        self.weight = weight
        self.sprite = pygame.image.load("templates/vertex.png")
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.rect = self.sprite.get_rect()#tem que pegar a coordenada do sprite e setar de acordo com a coordenada nova do vértice
        self.rect.x, self.rect.y = x * 60, y * 60
        self.x = x
        self.y = y
        self.highlight = highlight

    def getKey(self):
        return self.vertex

    def getWeight(self):
        return self.weight

    def setWeight(self, w):
        self.weight = w
    
    def setPos(self, x, y):
        self.x = x
        self.y = y
    def setHighlight(self, h):
        self.highlight = h
        if(h == True):
            self.sprite = pygame.image.load("templates/vertexHighlighted.png")
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.rect = self.sprite.get_rect()  # tem que pegar a coordenada do sprite e setar de acordo com a coordenada nova do vértice
            self.rect.x, self.rect.y = self.x * 60, self.y * 60
        else:
            self.sprite = pygame.image.load("templates/vertex.png")
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.rect = self.sprite.get_rect()  # tem que pegar a coordenada do sprite e setar de acordo com a coordenada nova do vértice
            self.rect.x, self.rect.y = self.x * 60, self.y * 60

    def getPos(self):
        return [self.x, self.y]
    def getRect(self):
        return self.rect


class Edge:

    def __init__(self, vertexA, vertexB, weight):
        self.edge = [vertexA, vertexB]
        self.weight = weight

    def setWeight(self, w):
        self.weight = w

    def getEdge(self):
        return self.edge


class Graph:

    def __init__(self, listOfVertex, listOfEdges):
        self.listOfEdges = listOfEdges
        self.listOfVertex = listOfVertex
        self.size = 0
        
        self.countSize(listOfVertex)

    def setVertex(self, key, weight):
        v = Vertex(key, weight)
        self.listOfVertex.append(v)

    def getVertex(self):
        return self.listOfVertex

    def getEdges(self):
        return self.listOfEdges
    
    def countSize(self, listV):

        size = len(listV)
        for i in listV:
            if i == 0:
                size -= 1
    
        self.size = size

    def getSize(self):
        return self.size

    def printGraph(self):
        print("Vertices")
        for v in self.listOfVertex:
            try:
                print(v.vertex)
            except AttributeError:
                print("Casa vazia")

        print("Edges")
        for e in self.listOfEdges:
            print(e.edge, e.weight)

    
