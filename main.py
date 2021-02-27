#Trabalho de APA
<<<<<<< HEAD
from collections import defaultdict
import graph

import pygame
def window():
    background_colour = (255,255,255)
    (width, height) = (1024, 576)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Trabalho de APA')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False


def buildGraph(data):
    vertexList = []
    edgeList = []
    for i in data:
        v = graph.Vertex(i, 1)
        for j in data[i]:
            e = graph.Edge(i, j, 1)
            edgeList.append(e)

        vertexList.append(v)

    g = graph.Graph(vertexList, edgeList)
    return g

def main():
    print("insira o grafo:")
    listGraph = input().split(";")

    graph = {}
=======
from matrix import Matrix

def main():
    listGraph = input().split(";")

    graph = {}
    sizeMatrix = 0
>>>>>>> origin/main

    for connection in listGraph:
        
        if(graph.get(connection[0])):
            graph[connection[0]].append(connection[2])
        else:
            graph[connection[0]] = [connection[2]]
<<<<<<< HEAD
        if (graph.get(connection[2])):
            graph[connection[2]].append(connection[0])
        else:
            graph[connection[2]] = [connection[0]]

    g = buildGraph(graph)
    g.printGraph()
    print(listGraph)
    print(graph)
    window()
=======
        
        if(graph.get(connection[2])):
            graph[connection[2]].append(connection[0])
        else:
            graph[connection[2]] = [connection[0]]
        
        if int(connection[0]) > sizeMatrix:
            sizeMatrix = int(connection[0])
        elif int(connection[2]) > sizeMatrix:
            sizeMatrix = int(connection[2]) 

    matrix = Matrix(graph, sizeMatrix)

    print(listGraph)
    print(graph)

>>>>>>> origin/main
main()