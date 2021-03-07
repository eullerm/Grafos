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
        self.rect.x = self.x = x
        self.rect.y = self.y = y

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
    def getHighlight(self):
        return self.highlight

class Edge:

    def __init__(self, vertexA, vertexB, weight, highlight):
        self.edge = [vertexA, vertexB]
        self.weight = weight
        self.sprite = pygame.image.load("templates/weight.png")
        self.sprite = pygame.transform.scale(self.sprite, (20, 20))
        self.highlight = highlight
        self.rect = self.sprite.get_rect()#tem que pegar a coordenada do sprite e setar de acordo com a coordenada nova do vértice
        self.rect.x, self.rect.y = 0, 0
        self.x = 0
        self.y = 0
        self.weightColor = (0,0,0)
    
    def setHighlight(self,h):
        self.highlight = h
        if h == True:
            self.weightColor = (255,0,0)
        else:
            self.weightColor =(0,0,0)

    def setPos(self, x, y):
        self.rect.x = self.x = x
        self.rect.y = self.y = y

    def getPos(self):
        return [self.x, self.y]
    
    def setWeight(self, w):
        self.weight = w

    def getWeight(self):
        return self.weight

    def getEdge(self):
        return self.edge

    def getHighlight(self):
        return self.highlight

class Graph:

    def __init__(self, data, size):
        self.listOfEdges = []
        self.listOfVertex = [-1] * size #O -1 é para poder desenhar vetores com vertices faltando
        self.size = 0
        
        self.buildGraph(data)

        self.countSize(self.listOfVertex)

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
        print("##############")

        print("Edges")
        for e in self.listOfEdges:
            print(e.edge, e.weight)
        print("##############")

    def buildGraph(self, data):
         
        for i in data:
            v = Vertex(i, 1, 0, 0, False)
            for j in data[i]:
                if(not self.isSet(self.listOfEdges, [i, j])):   
                    e = Edge(i, j, 1, False)
                    self.listOfEdges.append(e)
            self.listOfVertex[int(i) - 1] = v

    def isSet(self, listOfEdges, edge):

        for e in listOfEdges:
            v1 = e.getEdge()[0]
            v2 = e.getEdge()[1]

            if( (v1 == edge[0] or v1 == edge[1]) and (v2 == edge[0] or v2 == edge[1])):
                return True

        return False


    
