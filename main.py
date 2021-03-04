#Trabalho de APA
from collections import defaultdict
import graph
import matrix
import math

import pygame


def window(graph):
    pygame.init()
    pygame.display.init()
    background_colour = (255,255,255)
    (width, height) = (1280, 720)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Trabalho de APA')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        drawGraph(graph, screen)
        pygame.display.flip()


def drawGraph(graph, screen):
    vertexList = graph.getVertex()
    allSpritesList = pygame.sprite.Group()
    Rects = pygame.sprite.Group()
    sprites = []
    for s in vertexList:
        screen.blit(s.sprite, (s.x, s.y))




def buildGraph(data):
    vertexList = []
    edgeList = []
    for i in data:
        positions = []
        for j in vertexList:
            positions.append(j.getPos())
        p = [10, 10]
        for j in range(len(positions)):
            x = 70
            y = 70
            a = 0
            b = 0
            if p == positions[j]:
                if j % 2 == 0:
                    a+=1
                    if (a > math.sqrt(len(data))):
                        x+=70
                else:
                    b+=1
                    if (b > math.sqrt(len(data))):
                        y+=70

            p = [p[0] + x, p[1] + y]


        v = graph.Vertex(i, 1,  p[0], p[1], False)
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

from matrix import Matrix

def main():
    listGraph = input().split(";")

    graph = {}
    sizeMatrix = 0


    for connection in listGraph:
        
        if(graph.get(connection[0])):
            graph[connection[0]].append(connection[2])
        else:
            graph[connection[0]] = [connection[2]]

        if (graph.get(connection[2])):
            graph[connection[2]].append(connection[0])
        else:
            graph[connection[2]] = [connection[0]]
        
        if int(connection[0]) > sizeMatrix:
            sizeMatrix = int(connection[0])
        elif int(connection[2]) > sizeMatrix:
            sizeMatrix = int(connection[2]) 

    matrix = Matrix(graph, sizeMatrix)
    g = buildGraph(graph)
    g.printGraph()
    print(listGraph)
    print(graph)
    window(g)


main()