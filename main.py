#Trabalho de APA
from graph import Graph
from matrix import Matrix
import pygame, sys
import math
from math import cos, pi, radians, sin

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NUMBER_COLOR = (0, 0, 255)

SQUARE_COLOR = (80, 80, 0)

TOP = 80
WIDTH = 60
HEIGHT = 60
MARGIN = 10

def keyInput(event, object, string):
    for o in object:
        if(o.getHighlight()):
            if event.key == pygame.K_0:
                string+='0'
            if event.key == pygame.K_1:
                string+='1'
            if event.key == pygame.K_2:
                string+='2'
            if event.key == pygame.K_3:
                string+='3'
            if event.key == pygame.K_4:
                string+='4'
            if event.key == pygame.K_5:
                string+='5'
            if event.key == pygame.K_6:
                string+='6'
            if event.key == pygame.K_7:
                string+='7'
            if event.key == pygame.K_8:
                string+='8'
            if event.key == pygame.K_9:
                string+='9'
            if event.key == pygame.K_RETURN:
                o.setWeight(string)
    return string

def window(view, graph, matrix):

    pygame.font.init()
    string = ''
    
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

        SQUARE1 = pygame.Rect(MARGIN, MARGIN/2, 3 * WIDTH + 2 * MARGIN, TOP)
        pygame.draw.rect(screen, BLACK, SQUARE1 )
        screen.blit(BUTTON1, (WIDTH/2 + 4 * MARGIN, TOP/2))
        
        SQUARE2 = pygame.Rect(3 * WIDTH + 4 * MARGIN, MARGIN/2, 3 * WIDTH + 2 * MARGIN, TOP) 
        pygame.draw.rect(screen, BLACK, SQUARE2)
        screen.blit(BUTTON2, (3 * WIDTH + 7 * MARGIN, TOP/2))
        
        SQUARE3 = pygame.Rect(6 * WIDTH + 7 * MARGIN, MARGIN/2, 3 * WIDTH + 2 * MARGIN, TOP) 
        pygame.draw.rect(screen, BLACK, SQUARE3)
        screen.blit(BUTTON3, (6 * WIDTH + 10 * MARGIN, TOP/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                string = keyInput(event, graph.getVertex(), string)
                string = keyInput(event, graph.getEdges(), string)
                print(string)

            if event.type == pygame.MOUSEBUTTONDOWN:
                string =''
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
                        if s.highlight == True:
                            s.setHighlight(False)
                        if s.rect.collidepoint(event.pos):
                            s.setHighlight(True)
                for e in graph.getEdges():
                    print(e.getPos())
                    print(e.sprite.get_rect().x)
                    if e.highlight == True:
                        e.setHighlight(False)
                    if e.rect.collidepoint(event.pos):
                        e.setHighlight(True)
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

            screen.blit(text, ( (MARGIN + WIDTH) * column + MARGIN + fontSize/3,
                            (MARGIN + HEIGHT) * row + TOP + fontSize/3,
                            ))

def drawGraph(graph, screen):

    pygame.font.init()
    fontSize = 30
    RED = (255, 0, 0)
    font = pygame.font.SysFont('arial', fontSize)
    font2 = pygame.font.SysFont('arial', int(fontSize/2)+5)

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
            #s.setPos(x - s.sprite.get_width()/2, y - s.sprite.get_height()/2)#Da um set para a posição do sprite
            s.setPos(x, y)
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

                line = pygame.draw.line(screen, BLACK, (vertexAx, vertexAy), (vertexBx, vertexBy), 1)

                textX = 0
                textY = 0

                if(vertexAx < centerX and vertexAy == centerY):
                    textX = -28
                
                elif(vertexBx > centerY and vertexBx == centerX):
                    textX = 20

                if( (vertexAx - vertexBx) == 0):
                    textX = -40
                    textY = -2
                if( (vertexAy - vertexBy) == 0):
                    textX = 2
                    textY = -60
                e.setPos(line.centerx + textX, line.centery + textY)
                screen.blit(e.sprite, e.getPos())
                textWeight = font2.render(str(e.getWeight()), True, e.weightColor)
                screen.blit(textWeight, (line.centerx + textX, line.centery + textY))
               
            except IndexError:
                print(vertexA, vertexB)
    
    for s in vertexList:

        if(s != -1):
            PURPLE = (127, 0, 255)
            screen.blit(s.sprite, s.getPos())
            text = font.render(str(s.vertex), True, NUMBER_COLOR)
            textWeight = font2.render(str(s.getWeight()), True, PURPLE)

            textX = 0
            textY = 0

            screen.blit(text, (s.getPos()[0] + 15, s.getPos()[1] + 8))
            screen.blit(textWeight, (s.rect.x+18, s.rect.y-15))
            
        


def main():

    # 1 - Visualiza o grafo
    # 2 - Para visualizar a matrizes de adjacencia
    # 3 - Para visualizar a matriz de incidencia
    view = 1

    print("insira o grafo:")

    listGraph = input().split(";")

    matrix = Matrix(listGraph)

    print(listGraph)

    graph = Graph(matrix.getGraph(), matrix.getSize())

    graph.printGraph()
    print(listGraph)
    window(view, graph, matrix)

main()