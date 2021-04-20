from matrix import Matrix
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
            self.weightColor = (0,0,0)

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
        self.data = data

        self.graphKruskalMST = list()
        self.listOfEdgesKruskal = []
        self.listOfVertexKruskal = [-1] * size

        self.graphPrimMST = list()
        self.listOfEdgesPrim = []
        self.listOfVertexPrim = [-1] * size

        self.countSize(self.listOfVertex)
        self.buildGraph(data) #Passa a matriz para construir o grafo 
        #self.kruskalMST(data)
        self.kruskal = []
        self.prim = []

    def setVertex(self, key, weight):
        v = Vertex(key, weight)
        self.listOfVertex.append(v)

    def getVertex(self):
        return self.listOfVertex

    def getEdges(self):
        return self.listOfEdges
    
    def getEdgesKruskal(self):
        return self.listOfEdgesKruskal
    
    def getEdgesPrim(self):
        return self.listOfEdgesPrim
    
    def countSize(self, listV): #Conta o tamanho real do grafo

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
        print("Arestas")
        for e in self.listOfEdges:
            print(e.edge, e.weight)
        print("##############")

    def buildGraph(self, data):

        graph = data.getGraph() 
        
        for i in graph:
            v = Vertex(i, 1, 0, 0, False)
            for j in graph[i]:
                if(not self.isSet(self.listOfEdges, [i, j])):   
                    e = Edge(i, j, data.getWeight(int(i)-1, int(j)-1), False)
                    self.listOfEdges.append(e)
            self.listOfVertex[int(i) - 1] = v

    def isSet(self, listOfEdges, edge):

        for e in listOfEdges:
            v1 = e.getEdge()[0]
            v2 = e.getEdge()[1]

            if( (v1 == edge[0] or v1 == edge[1]) and (v2 == edge[0] or v2 == edge[1])):
                return True

        return False

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's
        # algorithm
    def kruskalMST(self):
          
        # An index variable, used for sorted edges
        i = 0
         
        # An index variable, used for result[]
        e = 0
 
        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        graph = list()
        for edge in self.listOfEdges:
            graph.append([int(edge.edge[0])-1, int(edge.edge[1])-1, int(edge.weight)])#Pega os vertices e os pesos [v1, v2, p]
        # given graph, we can create a copy of graph
        ordered = sorted(graph,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.size):
            parent.append(node)
            rank.append(0)
 
        # Number of edges to be taken is equal to V-1
        while e < self.size - 1:
 
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            line=[]
            u, v, w = ordered[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            line.append([["found " + str(u) + " on position " + str(x)], ["found " + str(y) + " on position " + str(parent[v])+" "]])
            # If including this edge does't
            #  cause cycle, include it in result
            #  and increment the indexof result
            # for next edge
            if x != y:
                line.append([[str(u)+" and "+str(v)+" are not in the same tree"], [" union("+str(u)+", "+str(v)+")"]])
                e = e + 1
                self.graphKruskalMST.append([int(u) + 1, int(v) + 1, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
            else:
                line.append([[str(u)+" and "+str(v)+"are in the same tree, do nothing."]])
            self.kruskal.append(line)
        minimumCost = 0
        print ("Arestas da arvore minima")
        for u, v, weight in self.graphKruskalMST:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Arvore minima com custo " , minimumCost)
        #print("#########################")

        for i in self.graphKruskalMST:
            v = Vertex(i[0], 1, 0, 0, False)
            v2 = Vertex(i[1], 1, 0, 0, False)
            if(not self.isSet(self.listOfEdgesKruskal, [i[0], i[1]])):   
                e = Edge(i[0], i[1], self.data.getWeight(int(i[0])-1, int(i[1])-1), False)
                self.listOfEdgesKruskal.append(e)
            self.listOfVertexKruskal[int(i[0]) - 1] = v
            self.listOfVertexKruskal[int(i[1]) - 1] = v2


    def getKruskal(self):
        return self.graphKruskalMST
    def getKruskalSteps(self):
        return self.kruskal
    
    def primMST(self):

        INF = 9999999
        # number of vertices in graph
        V = 5
        # create a 2d array of size 5x5
        # for adjacency matrix to represent graph
        G = self.data.getAdjacencyMatrix()
        # create a array to track selected vertex
        # selected will become true otherwise false
        selected = [0] * self.size
        # set number of edge to 0
        no_edge = 0
        # the number of egde in minimum spanning tree will be
        # always less than(V - 1), where V is number of vertices in
        # graph
        # choose 0th vertex and make it true
        selected[0] = True
        # print for edge and weight
        print("Aresta : Peso\n")
        while (no_edge < self.size - 1):
            # For every vertex in the set S, find the all adjacent vertices
            #, calculate the distance from the vertex selected at step 1.
            # if the vertex is already in the set S, discard it otherwise
            # choose another vertex nearest to selected vertex  at step 1.
            minimum = INF
            x = 0
            y = 0
            for i in range(self.size):
                if selected[i]:
                    for j in range(self.size):
                        if ((not selected[j]) and G[i][j]):  
                            # not in selected and there is an edge
                            if minimum > G[i][j]:
                                minimum = G[i][j]
                                x = i
                                y = j
            
            self.graphPrimMST.append([int(x) + 1, int(y) + 1, int(G[x][y])])
            for i in self.graphPrimMST:
                v = Vertex(i[0], 1, 0, 0, False)
                v2 = Vertex(i[1], 1, 0, 0, False)
                if(not self.isSet(self.listOfEdgesPrim, [i[0], i[1]])):   
                    e = Edge(i[0], i[1], G[x][y], False)
                    self.listOfEdgesPrim.append(e)
                self.listOfVertexPrim[int(i[0]) - 1] = v
                self.listOfVertexPrim[int(i[1]) - 1] = v2
            print(str(x+1) + "-" + str(y+1) + ":" + str(G[x][y]))
            selected[y] = True
            no_edge += 1