class Vertex:

    def __init__(self, vertex, listOfVertex):
        self.dots = []
        

    def setAllVertex(self, vertex, listOfVertex):
        i=0
        for dotA in vertex:
            for dotB in listOfVertex[i]:
                if dotB not in self.dots:
                    self.dots.append(dotB)
            i+=1

class Edge: 
    def __init__(self, dotA, dotB, weight):
        self.edge = [dotA, dotB]
        self.weight = weight



class Graph:

    def __init__(self, vertex, listOfVertex, weight):
        self.vertex = Vertex()