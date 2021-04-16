#Trabalho de APA

####

import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

#####

from graph import Graph
from matrix import Matrix
import pygame
from math import cos, pi, radians, sin

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NUMBER_COLOR = (0, 0, 255)
RED = (180, 0, 0)
GREEN = (0, 180, 0)
SQUARE_COLOR = (80, 80, 0)

WINDOW_SIZE = (1280, 800)
TOP = 80
WIDTH = 60
HEIGHT = 60
MARGIN = 10

def keyInput(event, object, string, object2 = False):
    for o in object:
        if(o != -1):
            if(o.getHighlight()):
                if event.key == pygame.K_0:
                    string += '0'
                if event.key == pygame.K_1:
                    string += '1'
                if event.key == pygame.K_2:
                    string += '2'
                if event.key == pygame.K_3:
                    string += '3'
                if event.key == pygame.K_4:
                    string += '4'
                if event.key == pygame.K_5:
                    string += '5'
                if event.key == pygame.K_6:
                    string += '6'
                if event.key == pygame.K_7:
                    string += '7'
                if event.key == pygame.K_8:
                    string += '8'
                if event.key == pygame.K_9:
                    string += '9'
                if event.key == pygame.K_RETURN:
                    string = int(string)
                    o.setWeight(string)
                    if(object2):
                        object2.changeWeight(int(o.getEdge()[0]),int(o.getEdge()[1]), string)
    return string

def window(view, graph, matrix):

    pygame.font.init()
    string = ''
    
    fontSize = 15
    font2 = pygame.font.SysFont('arial', fontSize)

    BUTTON1 = font2.render("Grafo", True, WHITE)
    BUTTON2 = font2.render("Kruskal", True, WHITE)
    BUTTON3 = font2.render("Prim", True, WHITE)
    BUTTON4 = font2.render("Matriz de adjacência", True, WHITE)
    BUTTON5 = font2.render("Matriz de incidência", True, WHITE)
    BUTTON6 = font2.render("Voltar", True, WHITE)
    
    pygame.display.set_caption('Trabalho de APA')
    
    running = True
    
    while running:

        screen = pygame.display.set_mode(WINDOW_SIZE)
        screen.fill(WHITE)

        SQUARE1 = pygame.Rect(MARGIN, MARGIN/2, 3 * WIDTH + 2 * MARGIN, TOP)
        pygame.draw.rect(screen, BLACK, SQUARE1 )
        screen.blit(BUTTON1, (WIDTH/2 + 4 * MARGIN, TOP/2))
        
        SQUARE2 = pygame.Rect(3 * WIDTH + 4 * MARGIN, MARGIN/2, 3 * WIDTH + 2 * MARGIN, TOP) 
        pygame.draw.rect(screen, BLACK, SQUARE2)
        screen.blit(BUTTON2, (3 * WIDTH + 7 * MARGIN, TOP/2))
        
        SQUARE3 = pygame.Rect(6 * WIDTH + 7 * MARGIN, MARGIN/2, 3 * WIDTH + 2 * MARGIN, TOP) 
        pygame.draw.rect(screen, BLACK, SQUARE3)
        screen.blit(BUTTON3, (6 * WIDTH + 10 * MARGIN, TOP/2))

        SQUARE4 = pygame.Rect(9 * WIDTH + 10 * MARGIN, MARGIN/2, 3 * WIDTH + 2 * MARGIN, TOP) 
        pygame.draw.rect(screen, BLACK, SQUARE4)
        screen.blit(BUTTON4, (9 * WIDTH + 13 * MARGIN, TOP/2))
    
        SQUARE5 = pygame.Rect(12 * WIDTH + 13 * MARGIN, MARGIN/2, 3 * WIDTH + 2 * MARGIN, TOP) 
        pygame.draw.rect(screen, BLACK, SQUARE5)
        screen.blit(BUTTON5, (12 * WIDTH + 16 * MARGIN, TOP/2))

        SQUARE6 = pygame.Rect(15 * WIDTH + 16 * MARGIN, MARGIN/2, 3 * WIDTH + 2 * MARGIN, TOP) 
        pygame.draw.rect(screen, BLACK, SQUARE6)
        screen.blit(BUTTON6, (15 * WIDTH + 18 * MARGIN, TOP/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                string = keyInput(event, graph.getVertex(), string)
                string = keyInput(event, graph.getEdges(), string, matrix)
                print(string)

            if event.type == pygame.MOUSEBUTTONDOWN:
                string =''
                print(event.pos)
                if SQUARE1.collidepoint(event.pos):
                    view = 1
                    graph = Graph(matrix, matrix.getSize())
                elif SQUARE2.collidepoint(event.pos):
                    view = 2    
                    graph = Graph(matrix, matrix.getSize())
                    graph.kruskalMST()
                elif SQUARE3.collidepoint(event.pos):
                    view = 3 
                    graph = Graph(matrix, matrix.getSize())
                    graph.primMST()
                elif SQUARE4.collidepoint(event.pos):
                    view = 4 
                elif SQUARE5.collidepoint(event.pos):
                    view = 5 

                elif SQUARE4.collidepoint(event.pos):
                    running = False
                for s in graph.getVertex():
                    if(s != -1):
                        if s.getHighlight():
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

        if(view == 1 or view == 2 or view == 3):
            drawGraph(graph, screen, view)

        elif(view == 4 or view == 5):#Matriz de adjacencia/incidencia
            drawMatrix(matrix, screen, view-3)


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

def drawGraph(graph, screen, flag):

    pygame.font.init()
    fontSize = 30
    RED = (255, 0, 0)
    font = pygame.font.SysFont('arial', fontSize)
    font2 = pygame.font.SysFont('arial', int(fontSize/2)+5)

    centerX = screen.get_width() /2
    centerY = screen.get_height() / 2
    radius = 200
    vertexList = graph.getVertex()
    
    if (flag == 1):
        edgeList = graph.getEdges()
    elif(flag == 2):
        edgeList = graph.getEdgesKruskal()
    elif(flag == 3):
        edgeList = graph.getEdgesPrim()

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
            

        if(vertexA != vertexB and vertexA and vertexB):
            try:
                vertexAx = vertexList[vertexA - 1].getPos()[0] + 25
                vertexAy = vertexList[vertexA - 1].getPos()[1] + 25
                vertexBx = vertexList[vertexB - 1].getPos()[0] + 25
                vertexBy = vertexList[vertexB - 1].getPos()[1] + 25

                line = pygame.draw.line(screen, BLACK, (vertexAx, vertexAy), (vertexBx, vertexBy), 1)

                textX = 0
                textY = 0

                if( (vertexAx - vertexBx) == 0):
                    textX = 2
                    textY = -60
                if( (vertexAy - vertexBy) == 0):
                    textX = -40
                    textY = -2

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
            
def showGraph(inputGraph):
    listGraph = inputGraph.split(";")
    matrix = Matrix(listGraph)

    print(listGraph)

    graph = Graph(matrix.getGraph(), matrix.getSize())

    graph.printGraph()
    print(listGraph)
    window(1, graph, matrix)

def firstPage():

    exit = False

    pygame.font.init()
    fontSize = 15
    font = pygame.font.SysFont('arial', fontSize)

    BUTTON1 = font.render("Criar grafo", True, WHITE)
    BUTTON2 = font.render("Sair", True, WHITE)
    TEXT = font.render("Digite aqui o grafo. Exemplo: 1-2;3-4", True, BLACK)


    inputGraph = ''
    pressed = False

    while not exit:
        screen = pygame.display.set_mode(WINDOW_SIZE)
        screen.fill(WHITE)

        INPUT = pygame.Rect(WINDOW_SIZE[0]/2 - 240, WINDOW_SIZE[1]/2 - 100, 500, TOP)
        pygame.draw.rect(screen, BLACK, INPUT)
        pygame.draw.rect(screen, WHITE, (WINDOW_SIZE[0]/2 - 235, WINDOW_SIZE[1]/2 - 95, 490, TOP - 10 ))
        screen.blit(TEXT, (WINDOW_SIZE[0]/2 - 230, WINDOW_SIZE[1]/2 - 70))

        SQUARE1 = pygame.Rect(WINDOW_SIZE[0]/2 - 100, WINDOW_SIZE[1]/2, 200, TOP)
        pygame.draw.rect(screen, GREEN, SQUARE1 )
        screen.blit(BUTTON1, (WINDOW_SIZE[0]/2 - 40, WINDOW_SIZE[1]/2 + 30))
        
        SQUARE2 = pygame.Rect(WINDOW_SIZE[0]/2 - 100, WINDOW_SIZE[1]/2 + 100, 200, TOP) 
        pygame.draw.rect(screen, RED, SQUARE2)
        screen.blit(BUTTON2, (WINDOW_SIZE[0]/2 - 20, WINDOW_SIZE[1]/2 + 130))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:

                if INPUT.collidepoint(event.pos):
                    pressed = True
                elif SQUARE1.collidepoint(event.pos):
                    showGraph(inputGraph)

                elif SQUARE2.collidepoint(event.pos):
                    exit = True

            if event.type == pygame.KEYDOWN:
                    print(pressed)
                    if pressed:
                        print(pressed)
                        if event.key == pygame.K_0:
                            inputGraph += '0'
                        if event.key == pygame.K_1:
                            inputGraph += '1'
                        if event.key == pygame.K_2:
                            inputGraph += '2'
                        if event.key == pygame.K_3:
                            inputGraph += '3'
                        if event.key == pygame.K_4:
                            inputGraph += '4'
                        if event.key == pygame.K_5:
                            inputGraph += '5'
                        if event.key == pygame.K_6:
                            inputGraph += '6'
                        if event.key == pygame.K_7:
                            inputGraph += '7'
                        if event.key == pygame.K_8:
                            inputGraph += '8'
                        if event.key == pygame.K_9:
                            inputGraph += '9'
                        if event.key == pygame.K_MINUS:
                            inputGraph += '-'
                        if event.key == pygame.K_SEMICOLON:
                            inputGraph += ';'
                        if event.key == pygame.K_BACKSPACE:
                            inputGraph = inputGraph[:len(inputGraph)-1]
                        if event.key == pygame.K_RETURN:
                            showGraph(inputGraph)

                    print(inputGraph)
                    TEXT = font.render(inputGraph, True, BLACK) 
                    screen.blit(TEXT, (WINDOW_SIZE[0]/2 - 230, WINDOW_SIZE[1]/2 - 70))

        pygame.display.flip()     

def main():

    #firstPage()
    
    # 1 - Visualiza o grafo
    # 2 - Kruskal
    # 3 - Prim
    # 4 - Para visualizar a matrizes de adjacencia
    # 5 - Para visualizar a matriz de incidencia
    view = 1

    print("insira o grafo:")

    listGraph = input().split(";")

    matrix = Matrix(listGraph)

    print(listGraph)

    graph = Graph(matrix, matrix.getSize())

    graph.printGraph()
    print(listGraph)
    window(view, graph, matrix)

main()