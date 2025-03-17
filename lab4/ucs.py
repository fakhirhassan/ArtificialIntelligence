import math
class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

def findMin(frontier):
    minV=math.inf
    node=''
    for i in frontier:
        if minV>frontier[i][1]:
            minV=frontier[i][1]
            node=i
    return node

def actionSequence(puzzle , initialState , goal ):
    solution = [goal]
    currentParent = puzzle[goal].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = puzzle[currentParent].parent
    solution.reverse()
    return solution


def UCS():
    initialState = 'Arad'
    goalState = 'Bucharest'
    
    romania_graph = {
    'Arad': Node('Arad', None, [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)], None),
    'Zerind': Node('Zerind', None, [('Arad', 75), ('Oradea', 71)], None),
    'Oradea': Node('Oradea', None, [('Zerind', 71), ('Sibiu', 151)], None),
    'Timisoara': Node('Timisoara', None, [('Arad', 118), ('Lugoj', 111)], None),
    'Lugoj': Node('Lugoj', None, [('Timisoara', 111), ('Mehadia', 70)], None),
    'Mehadia': Node('Mehadia', None, [('Lugoj', 70), ('Drobeta', 75)], None),
    'Drobeta': Node('Drobeta', None, [('Mehadia', 75), ('Craiova', 120)], None),
    'Craiova': Node('Craiova', None, [('Drobeta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)], None),
    'Rimnicu Vilcea': Node('Rimnicu Vilcea', None, [('Craiova', 146), ('Pitesti', 97), ('Sibiu', 80)], None),
    'Sibiu': Node('Sibiu', None, [('Arad', 140), ('Oradea', 151), ('Rimnicu Vilcea', 80), ('Fagaras', 99)], None),
    'Fagaras': Node('Fagaras', None, [('Sibiu', 99), ('Bucharest', 211)], None),
    'Pitesti': Node('Pitesti', None, [('Craiova', 138), ('Rimnicu Vilcea', 97), ('Bucharest', 101)], None),
    'Bucharest': Node('Bucharest', None, [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)], None),
    'Giurgiu': Node('Giurgiu', None, [('Bucharest', 90)], None),
    'Urziceni': Node('Urziceni', None, [('Bucharest', 85), ('Neamt', 87), ('Vaslui', 142)], None),
    'Neamt': Node('Neamt', None, [('Urziceni', 87)], None),
    'Vaslui': Node('Vaslui', None, [('Urziceni', 142), ('Iasi', 92)], None),
    'Iasi': Node('Iasi', None, [('Vaslui', 92), ('Neamt', 87)], None),
    'Hirsova': Node('Hirsova', None, [('Urziceni', 98), ('Eforie', 86)], None),
    'Eforie': Node('Eforie', None, [('Hirsova', 86)], None)
}
    frontier = dict()
    frontier[initialState] = (None,0)
    explored = []
    while len(frontier) != 0:
            currentNode = findMin(frontier)
            del frontier[currentNode]

            if romania_graph[currentNode].state == goalState:
                return actionSequence(romania_graph, initialState, goalState)

            explored.append(currentNode)

            for child in romania_graph[currentNode].actions:
                currentCost = child[1] + romania_graph[currentNode].totalCost

                if child[0] not in frontier and child[0] not in explored:
                    romania_graph[child[0]].parent = currentNode
                    romania_graph[child[0]].totalCost = currentCost
                    frontier[child[0]] = (romania_graph[child[0]].parent, romania_graph[child[0]].totalCost)

                elif child[0] in frontier:
                    if frontier[child[0]][1] < currentCost:
                        romania_graph[child[0]].parent = frontier[child[0]][0]
                        romania_graph[child[0]].totalCost = frontier[child[0]][1]
                    else:
                        frontier[child[0]] = (currentNode, currentCost)
                        romania_graph[child[0]].parent = frontier[child[0]][0]
                        romania_graph[child[0]].totalCost = frontier[child[0]][1]

solution = UCS()
print(solution)