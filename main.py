#Trabalho de APA
import graph
from matrix import Matrix
import pygame, sys
import math
from math import cos, pi, radians, sin

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NUMBER_COLOR = (0, 0, 255)
SQUARE_COLOR = (80, 80, 0)

TOP = 80

def window(view, graph, matrix):

    pygame.font.init()
    fontSize = 50
    font = pygame.font.SysFont('arial', fontSize)

    font2 = pygame.font.SysFont('arial', int(fontSize/5)+5)

    BUTTON1 = font2.render("Grafo", True, WHITE)
    BUTTON2 = font2.render("Matriz de adjacência", True, WHITE)
    BUTTON3 = font2.render("Matriz de incidência", True, WHITE)

 
    background_color = WHITE
    
    pygame.display.set_caption('Trabalho de APA')
    
    WINDOW_SIZE = (1280, 800)


    WIDTH = 80
    HEIGHT = 80
    MARGIN = 10
    
    
    running = True
    
    while running:

        screen = pygame.display.set_mode(WINDOW_SIZE)
        screen.fill(background_color)

        SQUARE1 = pygame.Rect(MARGIN, MARGIN/2, 2 * WIDTH + MARGIN, TOP)
        pygame.draw.rect(screen, BLACK, SQUARE1 )
        screen.blit(BUTTON1, (WIDTH/2 + 3 * MARGIN, TOP/2))
        
        SQUARE2 = pygame.Rect(2 * WIDTH + 3 * MARGIN, MARGIN/2, 2 * WIDTH + MARGIN, TOP) 
        pygame.draw.rect(screen, BLACK, SQUARE2)
        screen.blit(BUTTON2, (2 * WIDTH + 5 * MARGIN, TOP/2))
        
        SQUARE3 = pygame.Rect(4 * WIDTH + 5 * MARGIN, MARGIN/2, 2 * WIDTH + MARGIN, TOP) 
        pygame.draw.rect(screen, BLACK, SQUARE3)
        screen.blit(BUTTON3, (4 * WIDTH + 7 * MARGIN, TOP/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if SQUARE1.collidepoint(event.pos):
                    view = 1
                elif SQUARE2.collidepoint(event.pos):
                    view = 2
                elif SQUARE3.collidepoint(event.pos):
                    view = 3

        if(view == 1):
            WINDOW_SIZE = (1280, 800)
            
            drawGraph(graph, screen)

        elif(view == 2 or view == 3):

            windowWidth = (WIDTH + MARGIN) * matrix.getSize() + MARGIN

            if(windowWidth > 550):
                WINDOW_SIZE = (windowWidth , (HEIGHT + MARGIN) * matrix.getSize() + MARGIN + TOP)
            else:
                WINDOW_SIZE = (550 , (HEIGHT + MARGIN) * matrix.getSize() + MARGIN + TOP)
        
            for row in range(matrix.getSize()):
                for column in range(matrix.getSize()):
                    pygame.draw.rect(screen,
                                    SQUARE_COLOR,
                                    [(MARGIN + WIDTH) * column + MARGIN,
                                    (MARGIN + HEIGHT) * row + MARGIN + TOP,
                                    WIDTH,
                                    HEIGHT])

                    text = font.render(str(matrix.getValue(row, column, view-1)), True, NUMBER_COLOR)

                    screen.blit(text, ( (MARGIN + WIDTH) * column + MARGIN + fontSize/2,
                                    (MARGIN + HEIGHT) * row + TOP + fontSize/2,
                                    ))
                    
        pygame.display.flip()     


def drawGraph(graph, screen):

    pygame.font.init()
    fontSize = 50
    font = pygame.font.SysFont('arial', fontSize)

    centerX = screen.get_width() /2
    centerY = screen.get_height() / 2
    radius = 200
    vertexList = graph.getVertex()
    edgeList = graph.getEdges()
    angle = radians(0)
    rotate = radians(360 / graph.getSize())

    x = centerX - radius * cos(angle)
    y = centerY - radius * sin(angle)
    
    #Centro do circulo
    pygame.draw.rect(screen, BLACK, [centerX, centerY, 10, 10])

    allSpritesList = pygame.sprite.Group()
    Rects = pygame.sprite.Group()
    sprites = []
    
    for s in vertexList:
        if(s != 0):
            s.setPos(x - s.sprite.get_width()/2, y - s.sprite.get_height()/2)#Da um set para a posição do sprite
    
            angle += rotate
            x = centerX - radius * cos(angle)
            y = centerY - radius * sin(angle)
    
    for e in edgeList:

        vertexA = int(e.getEdge()[0])
        vertexB = int(e.getEdge()[1])

        if(vertexA != vertexB):
            try:
                vertexAx = vertexList[vertexA - 1].getPos()[0] + 25
                vertexAy = vertexList[vertexA - 1].getPos()[1] + 25
                vertexBx = vertexList[vertexB - 1].getPos()[0] + 25
                vertexBy = vertexList[vertexB - 1].getPos()[1] + 25

                pygame.draw.line(screen, BLACK, (vertexAx, vertexAy), (vertexBx, vertexBy), 1)
            except IndexError:
                print(vertexA, vertexB)
    
    for s in vertexList:

        if(s != 0):
            screen.blit(s.sprite, s.getPos())
            text = font.render(str(s.vertex), True, NUMBER_COLOR)

            screen.blit(text, (s.getPos()[0] + 10, s.getPos()[1]))
        

        

def buildGraph(data, size):
    vertexList = [0] * size
    edgeList = []
    for i in data:
        v = graph.Vertex(i, 1, 0, 0, False)
        for j in data[i]:
            e = graph.Edge(i, j, 1)
            edgeList.append(e)
        vertexList[int(i) - 1] = v

    g = graph.Graph(vertexList, edgeList)
    return g


def main():

    # 1 - Visualiza o grafo
    # 2 - Para visualizar a matrizes de adjacencia
    # 3 - Para visualizar a matriz de incidencia
    view = 1

    print("insira o grafo:")

    listGraph = input().split(";")

    graph = {}
    matrixSize = 0


    for connection in listGraph:
        
        if(graph.get(connection[0])):
            graph[connection[0]].append(connection[2])
        else:
            graph[connection[0]] = [connection[2]]

        if (graph.get(connection[2])):
            graph[connection[2]].append(connection[0])
        else:
            graph[connection[2]] = [connection[0]]
        
        if int(connection[0]) > matrixSize:
            matrixSize = int(connection[0])
            
        if int(connection[2]) > matrixSize:
            matrixSize = int(connection[2]) 
            

    matrix = Matrix(graph, matrixSize)

    print(listGraph)
    print(graph)


    g = buildGraph(graph, matrixSize)
    g.printGraph()
    print(listGraph)
    print(graph)
    window(view, g, matrix)

main()