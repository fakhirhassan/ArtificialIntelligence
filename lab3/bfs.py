class Node:
    def __init__(self,state,parent,actions,totalcost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalcost = totalcost
        
        
        
# def BFS():
#     initialState = 'D'
#     goal = 'F'
#     graph = {
#     'A' : Node('A' , None , ['B' , 'C' , 'E'], None), 
#     'B' : Node('B' , None , ['A' , 'D' ,'E'] , None),
#     'C' : Node('C' , None , ['A' , 'F' , 'G'] , None),
#     'D' : Node('D' , None , ['B' , 'E'] , None),
#     'E' : Node('E' , None , ['A' , 'B' , 'D'] , None),
#     'F' : Node('F' , None , ['C'] , None),
#     'G' : Node('G' , None , ['C'] , None)

# }
#     frontier = [initialState]
#     explored = []

#     while len(frontier)!=0:
#         currentNode = frontier.pop(0)
#         explored.append(currentNode)
#         for child in graph[currentNode].actions:
#             if child not in frontier and child not in explored:
#                 graph[child].parent = currentNode
#                 if graph[child].state == goal:
#                     return actionSequence(graph , initialState , goal)
#                 frontier.append(child)


# def actionSequence(graph , initialState , goal ):
#     solution = [goal]
#     currentParent = graph[goal].parent
#     while currentParent != None:
#         solution.append(currentParent)
#         currentParent = graph[currentParent].parent
#     solution.reverse()
#     return solution

# solution = BFS()
# print(solution)


def BFS():
    initialState = 'Arad'
    goal = 'Bucharest'

    
    romania_graph = {
        'Arad': Node('Arad', None, ['Zerind', 'Timisoara', 'Sibiu'] ,None),
        'Zerind': Node('Zerind', None, ['Arad', 'Oradea'],None),
        'Oradea': Node('Oradea', None, ['Zerind', 'Sibiu'],None),
        'Timisoara': Node('Timisoara', None, ['Arad', 'Lugoj'],None),
        'Lugoj': Node('Lugoj', None, ['Timisoara', 'Mehadia'],None),
        'Mehadia': Node('Mehadia', None, ['Lugoj', 'Drobeta'],None),
        'Drobeta': Node('Drobeta', None, ['Mehadia', 'Craiova'],None),
        'Craiova': Node('Craiova', None, ['Drobeta', 'Pitesti', 'Rimnicu Vilcea'],None),
        'Rimnicu Vilcea': Node('Rimnicu Vilcea', None, ['Craiova', 'Pitesti', 'Sibiu'],None),
        'Sibiu': Node('Sibiu', None, ['Arad', 'Oradea', 'Rimnicu Vilcea', 'Fagaras'],None),
        'Fagaras': Node('Fagaras', None, ['Sibiu', 'Bucharest'],None),
        'Pitesti': Node('Pitesti', None, ['Craiova', 'Rimnicu Vilcea', 'Bucharest'],None),
        'Bucharest': Node('Bucharest', None, ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],None),
        'Giurgiu': Node('Giurgiu', None, ['Bucharest'],None),
        'Urziceni': Node('Urziceni', None, ['Bucharest', 'Neamt', 'Vaslui'],None),
        'Neamt': Node('Neamt', None, ['Urziceni'],None),
        'Vaslui': Node('Vaslui', None, ['Urziceni', 'Iasi'],None),
        'Iasi': Node('Iasi', None, ['Vaslui', 'Neamt'],None),
        'Hirsova': Node('Hirsova', None, ['Urziceni', 'Eforie'],None),
        'Eforie': Node('Eforie', None, ['Hirsova'],None)
    }
    frontier = [initialState]
    explored = []
    while len(frontier)!=0:
        currentNode = frontier.pop(0)
        explored.append(currentNode)
        for child in romania_graph[currentNode].actions:
            if child not in frontier and child not in explored:
                romania_graph[child].parent = currentNode
                if romania_graph[child].state == goal:
                    return actionSequence(romania_graph , initialState , goal)
                frontier.append(child)

def actionSequence(romania_graph , initialState , goal ):
    solution = [goal]
    currentParent = romania_graph[goal].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = romania_graph[currentParent].parent
    solution.reverse()
    return solution

solution = BFS()
print(solution)