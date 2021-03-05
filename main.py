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
WIDTH = 80
HEIGHT = 80
MARGIN = 10

def window(view, graph, matrix):

    pygame.font.init()
    
    fontSize = 15
    font2 = pygame.font.SysFont('arial', fontSize)

    BUTTON1 = font2.render("Grafo", True, WHITE)
    BUTTON2 = font2.render("Matriz de adjacência", True, WHITE)
    BUTTON3 = font2.render("Matriz de incidência", True, WHITE)

    background_color = WHITE
    
    pygame.display.set_caption('Trabalho de APA')
    
    WINDOW_SIZE = (1280, 800)
    
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
                    # Set the x, y postions of the mouse click
                x, y = event.pos
                for s in graph.getVertex():
                    if(s != -1):
                        print(s.rect)
                        if s.highlight == True:
                            s.setHighlight(False)
                        if s.rect.collidepoint(event.pos):
                            s.setHighlight(True)
                for s in graph.getVertex():
                    if(s != -1):
                        print(s.vertex, s.highlight)

        if(view == 1):
            #WINDOW_SIZE = (1280, 800)
            
            drawGraph(graph, screen)

        elif(view == 2 or view == 3):#Matriz de adjacencia

            #windowWidth = (WIDTH + MARGIN) * matrix.getSize() + MARGIN
                
            #if(windowWidth > 550):
            #    WINDOW_SIZE = (windowWidth , (HEIGHT + MARGIN) * matrix.getSize() + MARGIN + TOP)
            #else:
            #    WINDOW_SIZE = (550 , (HEIGHT + MARGIN) * matrix.getSize() + MARGIN + TOP)

            drawMatrix(matrix, screen, view-1)
                    
        pygame.display.flip()     

def drawMatrix(matrix, screen, flag):
    fontSize = 50
    font = pygame.font.SysFont('arial', fontSize)
    

    for row in range(matrix.getRow()):
        for column in range(matrix.getColumn(flag)):
            pygame.draw.rect(screen,
                            SQUARE_COLOR,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN + TOP,
                            WIDTH,
                            HEIGHT])

            text = font.render(str(matrix.getValue(row, column, flag)), True, NUMBER_COLOR)

            screen.blit(text, ( (MARGIN + WIDTH) * column + MARGIN + fontSize/2,
                            (MARGIN + HEIGHT) * row + TOP + fontSize/2,
                            ))

def drawGraph(graph, screen):

    pygame.font.init()
    fontSize = 40
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

    
    for s in vertexList:
        if(s != -1):
            s.setPos(x - s.sprite.get_width()/2, y - s.sprite.get_height()/2)#Da um set para a posição do sprite
            s.rect.x, s.rect.y = s.x, s.y
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

        if(s != -1):
            screen.blit(s.sprite, s.getPos())
            text = font.render(str(s.vertex), True, NUMBER_COLOR)

            screen.blit(text, (s.getPos()[0] + 15, s.getPos()[1]))
        

        

def buildGraph(data, size):
    vertexList = [-1] * size #O -1 é para poder desenhar vetores com vertices faltando
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

    matrix = Matrix(listGraph)

    print(listGraph)


    g = buildGraph(matrix.getGraph(), matrix.getSize())
    g.printGraph()
    print(listGraph)
    window(view, g, matrix)

main()