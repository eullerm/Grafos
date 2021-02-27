

class Matrix:
    def __init__(self, graph, tam):

        self.adjacencyMatrix = []
        self.incidenceMatrix = []

        lineAdjacency = []
        lineIncidence = []
        
        for i in range(tam):
            lineAdjacency = []
            lineIncidence = []
            for j in range(tam):
                lineAdjacency.append(0)
                lineIncidence.append(0)

            self.adjacencyMatrix.append(lineAdjacency)
            self.incidenceMatrix.append(lineIncidence)

        self.initAdjacencyMatrix(graph)

        self.initIncidenceMatrix(graph)

    def initAdjacencyMatrix(self, graph):

        for key in graph.keys():
            for value in graph[key]:
                self.adjacencyMatrix[int(key)-1][int(value)-1] = 1 
        
        print(self.adjacencyMatrix)

        
        
    def initIncidenceMatrix(self, graph):
    
        for key in graph.keys():
            for value in graph[key]:
                if(key == value):
                    self.incidenceMatrix[int(key)-1][int(value)-1] = 2
                else:  
                    self.incidenceMatrix[int(key)-1][int(value)-1] = 1
        print(self.incidenceMatrix)
