#Classe para construção das matrizes de adjacencia e incidencia

class Matrix:
    def __init__(self, graph, size):

        self.adjacencyMatrix = []
        self.incidenceMatrix = []
        self.matrixSize = size

        lineAdjacency = []
        lineIncidence = []
        
        for i in range(size):
            lineAdjacency = []
            lineIncidence = []
            for j in range(size):
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

    def getSize(self):
        return self.matrixSize


    def getValue(self, row, column, flag):

        if (flag == 1):
            return self.adjacencyMatrix[row][column]
        elif(flag == 2):
            return self.incidenceMatrix[row][column]

    #Caso mude o peso da aresta
    def changeWeigth(self, v1, v2, newWeigth):
        self.adjacencyMatrix[v1][v2] = newWeigth
        self.adjacencyMatrix[v2][v1] = newWeigth