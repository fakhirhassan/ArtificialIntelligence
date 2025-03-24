class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost



graph = {
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
    
listWord = ['START','NOTE', 'SAND', 'STONE1D']
   
def generateWords(graph, listWord):
    valid_words = set()

    def dfs(currentNode, path, visited, current_word):
        if current_word in listWord:
            valid_words.add(current_word)

        for child in graph[currentNode].actions:
            if child not in visited:
                visited.add(child)
                dfs(child, path + [child], visited, current_word + graph[child].state)
                visited.remove(child)

    for node in graph:
        dfs(node, [node], set([node]), graph[node].state)

    return valid_words

valid_words = generateWords(graph, listWord)
print("Valid words found:", valid_words)


