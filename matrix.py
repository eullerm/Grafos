#Classe para construção das matrizes de adjacencia e incidencia

class Matrix:
    def __init__(self, listGraph):

        self.adjacencyMatrix = []
        self.incidenceMatrix = []
        self.matrixSize = 0
        self.row = 0
        self.adjacencyColumn = 0
        self.incidenceColumn = 0
        self.countEdge = 0
        self.graph = {}
        self.vertexEdge = {}

        self.createGraph(listGraph)

        for i in range(self.matrixSize):
            lineAdjacency = []
            lineIncidence = []
            for j in range(self.matrixSize):
                lineAdjacency.append(0)
            for j in range(self.countEdge):
                lineIncidence.append(0)

            self.adjacencyMatrix.append(lineAdjacency)
            self.incidenceMatrix.append(lineIncidence)

        self.initAdjacencyMatrix(self.graph)

        self.initIncidenceMatrix(self.graph, self.vertexEdge)

        
    
    
    
    def initAdjacencyMatrix(self, graph):

        for key in graph.keys():
            for value in graph[key]:
                self.adjacencyMatrix[int(key)-1][int(value)-1] = 1 
        
        print("###########")
        print("ADJACENCIA")
        print(self.adjacencyMatrix)
        print("###########")

    def initIncidenceMatrix(self, graph, vertexEdge):

        for key in graph.keys():
            for value in vertexEdge[key]:    
                self.incidenceMatrix[int(key)-1][int(value)] += 1 

        print("###########")
        print("INCIDENCIA")
        print(self.incidenceMatrix)
        print("###########")

    def getSize(self):
        return self.matrixSize

    def getRow(self):
        return self.row

    def getColumn(self, flag):
        if(flag == 1):
            return self.adjacencyColumn
        elif(flag == 2):
            return self.incidenceColumn

    def getValue(self, row, column, flag):

        if (flag == 1):
            return self.adjacencyMatrix[row][column]
        elif(flag == 2):
            return self.incidenceMatrix[row][column]

    #Caso mude o peso da aresta
    def changeWeigth(self, v1, v2, newWeigth):
        self.adjacencyMatrix[v1][v2] = newWeigth
        self.adjacencyMatrix[v2][v1] = newWeigth

    def createGraph(self, listGraph):

        for connection in listGraph:
            
            if(connection[0] != connection[2]):
            
                if(self.graph.get(connection[0]) and connection[2] not in self.graph.get(connection[0])):
                    self.graph[connection[0]].append(connection[2])
                    self.vertexEdge[connection[0]].append(self.countEdge)#Associa um vertice a uma aresta

                elif(not self.graph.get(connection[0])):
                    self.graph[connection[0]] = [connection[2]]
                    self.vertexEdge[connection[0]] = [self.countEdge]

                if (self.graph.get(connection[2]) and connection[0] not in self.graph.get(connection[2])):
                    self.graph[connection[2]].append(connection[0])
                    self.vertexEdge[connection[2]].append(self.countEdge)

                elif(not self.graph.get(connection[2])):
                    self.graph[connection[2]] = [connection[0]]            
                    self.vertexEdge[connection[2]] = [self.countEdge]
                
                if int(connection[0]) > self.matrixSize:
                    self.matrixSize = self.row = self.adjacencyColumn = int(connection[0])
                    
                if int(connection[2]) > self.matrixSize:
                    self.matrixSize = self.row = self.adjacencyColumn  = int(connection[2]) 
                
            
                self.countEdge += 1
                self.incidenceColumn = self.countEdge

    
    def getGraph(self):
        return self.graph