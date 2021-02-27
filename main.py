#Trabalho de APA
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

main()