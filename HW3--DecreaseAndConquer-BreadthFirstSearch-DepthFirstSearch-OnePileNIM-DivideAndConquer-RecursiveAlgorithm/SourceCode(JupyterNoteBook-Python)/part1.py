import pandas as pd
def ReadFiletoGrap(fileName):
    graph = {}
    rootVertex = None
    data = pd.read_excel(fileName)
    rootVertex = data.columns.values.tolist()[1]
    dataLists = data.values
    i = 2
    while (i < len(dataLists)):
        keyVertex = dataLists[i][0]
        val = set()
        while(i < len(dataLists) and keyVertex == dataLists[i][0]):
            val.add(dataLists[i][1])
            i += 1
        graph[keyVertex] = val
    return graph, rootVertex 

def DFS(graph, startVertex, visited=[]):
    if startVertex not in visited:
        visited.append(startVertex)
    if startVertex in graph:    
        for vertex in graph[startVertex] - set(visited):
            DFS(graph, vertex, visited)
    return visited

def BFS(graph, startVertex, queue=[], visited=[]):
    if startVertex not in queue and startVertex not in visited:
        queue.append(startVertex)
    
    for item in list(graph[startVertex]):
        if item not in queue and item not in visited:
            queue.append(item)

    startVertex = queue[0]
    queue.remove(startVertex)
    visited.append(startVertex)
    
    if(startVertex in graph):
        BFS(graph, startVertex, queue, visited)
        
    if(len(queue) > 0):
        startVertex = queue[0]
        queue.remove(startVertex)
        visited.append(startVertex)
        
    return visited

def PrintList(string,tList):
    print(string, end='')
    for i in range(0,len(tList)):
        if(i < len(tList)-1):
            print(str(tList[i]) + " -> ", end='')
        else:
            print(str(tList[i]))

def main():
    graph, rootVertex = ReadFiletoGrap('Graph_data.XLS')
    PrintList("BFS: ", BFS(graph, rootVertex))
    PrintList("DFS: ", DFS(graph, rootVertex))

if __name__ == "__main__":
    main()