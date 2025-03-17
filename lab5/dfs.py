class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

def actionSequence(romania_graph , initialState , goalstate ):
        solution = [goalstate]
        currentParent = romania_graph[goalstate].parent
        while currentParent != None:
            solution.append(currentParent)
            currentParent = romania_graph[currentParent].parent
        solution.reverse()
        return solution

def dfs():
    initialstate = 'Arad'
    goalstate = 'Bucharest'
    frontier = [initialstate]
    explored = []

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
    

    while len(frontier) != 0:
        currentNode = frontier.pop()
        print (currentNode)
        explored.append(currentNode)
        for child in romania_graph[currentNode].actions:
            if child not in frontier and child not in explored:
                romania_graph[child].parent = currentNode
                if child == goalstate:
                    print(explored)
                    return actionSequence(romania_graph, initialstate, goalstate)
                frontier.append(child)

solution = dfs()
print(solution)
