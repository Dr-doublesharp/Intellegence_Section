import queue as q

def a_star(graph,start,end):
    queue = q.PriorityQueue()
    queue.put((0,[start],[0,0])) # (cost,[path],[heuristic value, path value])
    while not queue.empty():
        node = queue.get() # (0,[start],[0,0])
        current = node[1][-1] # ['S','A','B'] -> 'B'

        if end == current:
            print('Path found: ' + str(node[1]) + ' With Cost Of: ' +str(node[0]) + " Heuristic value: " + str(node[2][0]) + " Path value of: " + str(node[2][1]))
            break

        for child in graph[current]:
            path = node[1][:] #-> Save Any Repeated Paths
            path.append(child) # p1 -> ['S','A']
            pathValue = node[2][1] + graph[current][child][1]
            heuristicValue = graph[current][child][0]
            queue.put((pathValue + heuristicValue, path, [heuristicValue,pathValue]))




graph = {
    'S': {'A':[9,3],'B':[1,1],'C':[3,5]},
    'A': {'E':[1,7],'G1':[0,10]},
    'B': {'C':[3,2],'F':[5,2]},
    'C': {'G3':[0,11]},
    'E': {'G1':[0,2]},
    'G1':{},
    'G2':{},
    'G3': {'F':[5,0]},
    'F': {'D':[4,1]},
    'D': {'B':[1,4],'G2':[0,5],'S':[8,6]}
}

a_star(graph,'S','G3')