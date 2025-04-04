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
    'M': Node('M', None, ['S', 'R','A'], None),
    'S': Node('S', None, ['M', 'E', 'R', 'A','T'], None),
    'E': Node('E', None, ['S', 'F', 'T', 'A','D'], None),
    'F': Node('F', None, ['E', 'D', 'T'], None),
    
    'R': Node('R', None, ['M', 'S', 'A', 'L','O'], None),
    'A': Node('A', None, ['S', 'E', 'T', 'N', 'L', 'R','O','M'], None),
    'T': Node('T', None, ['E', 'F', 'D', 'O', 'N', 'A','E','S'], None),
    'D': Node('D', None, ['F', 'T', 'E','N','E'], None),

    'L': Node('L', None, ['R', 'A', 'O', 'K','A1'], None),
    'O': Node('O', None, ['A', 'T', 'L', 'N','F','A','K','R'], None),
    'N': Node('N', None, ['T', 'D', 'F', 'O', 'E1', 'A', 'B', 'A'], None),
    'E': Node('E', None, ['D', 'T', 'N', 'F', 'B'], None),

    'K': Node('K', None, ['L', 'O', 'A'], None),
    'A': Node('A', None, ['N', 'L', 'F', 'K','O'], None),
    'F': Node('F', None, ['E', 'B', 'A','O','N'], None),
    'B': Node('B', None, ['F', 'E','N'], None)
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
