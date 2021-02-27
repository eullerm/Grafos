#Trabalho de APA
from collections import defaultdict



def main():
    listGraph = input().split(";")

    graph = {}

    for connection in listGraph:
        
        if(graph.get(connection[0])):
            graph[connection[0]].append(connection[2])
        else:
            graph[connection[0]] = [connection[2]]

    
    print(listGraph)
    print(graph)

main()