#Trabalho de APA
import graph
from matrix import Matrix
import pygame, sys
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

TOP = 80

def window(view, object):



    pygame.font.init()
    fontSize = 50
    font = pygame.font.SysFont('arial', fontSize)

    font2 = pygame.font.SysFont('arial', int(fontSize/5)+5)

    BUTTON1 = font2.render("Grafo", True, WHITE)
    BUTTON2 = font2.render("Matriz de adjacência", True, WHITE)
    BUTTON3 = font2.render("Matriz de incidência", True, WHITE)

 
    background_color = WHITE
    
    pygame.display.set_caption('Trabalho de APA')
    
    WIDTH = 80
    HEIGHT = 80
    MARGIN = 10

    if(view == 1):
        WINDOW_SIZE = (1280, 800)

    elif(view == 2 or view == 3):


        windowWidth = (WIDTH + MARGIN) * object.getSize() + MARGIN

        if(windowWidth > 550):
            WINDOW_SIZE = (windowWidth , (HEIGHT + MARGIN) * object.getSize() + MARGIN + TOP)
        else:
            WINDOW_SIZE = (550 , (HEIGHT + MARGIN) * object.getSize() + MARGIN + TOP)

    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(background_color)
    
    
    running = True
    
    while running:

        pygame.draw.rect(screen, BLACK, [MARGIN, MARGIN/2, 2 * WIDTH + MARGIN, TOP] )
        screen.blit(BUTTON1, (WIDTH/2 + 3 * MARGIN, TOP/2))
        
        pygame.draw.rect(screen, BLACK, [2 * WIDTH + 3 * MARGIN, MARGIN/2, 2 * WIDTH + MARGIN, TOP] )
        screen.blit(BUTTON2, (2 * WIDTH + 5 * MARGIN, TOP/2))
        
        pygame.draw.rect(screen, BLACK, [4 * WIDTH + 5 * MARGIN, MARGIN/2, 2 * WIDTH + MARGIN, TOP] )
        screen.blit(BUTTON3, (4 * WIDTH + 7 * MARGIN, TOP/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if(view == 1):
            drawGraph(object, screen)

        elif(view == 2 or view == 3):
            for row in range(object.getSize()):
                for column in range(object.getSize()):
                    pygame.draw.rect(screen,
                                    WHITE,
                                    [(MARGIN + WIDTH) * column + MARGIN,
                                    (MARGIN + HEIGHT) * row + MARGIN + TOP,
                                    WIDTH,
                                    HEIGHT])

                    text = font.render(str(object.getValue(row, column, view-1)), True, BLACK)

                    screen.blit(text, ( (MARGIN + WIDTH) * column + MARGIN + fontSize/2,
                                    (MARGIN + HEIGHT) * row + TOP + fontSize/2,
                                    ))
                    
        pygame.display.flip()     

def drawGraph(graph, screen):
    vertexList = graph.getVertex()
    allSpritesList = pygame.sprite.Group()
    Rects = pygame.sprite.Group()
    sprites = []
    for s in vertexList:
        screen.blit(s.sprite, (s.x, s.y + TOP))

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
            if p in positions:
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


    g = buildGraph(graph)
    g.printGraph()
    print(listGraph)
    print(graph)
    window(view, g)

main()