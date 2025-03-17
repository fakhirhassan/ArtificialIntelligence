class Node:
    def __init__(self,state,parent,actions,totalcost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalcost = totalcost

puzzle = {
        'node1': Node('node1', None, ['node2' , 'node24'], None),
        'node2': Node('node2', None, ['node1', 'node3'], None),
        'node3': Node('node3', None, ['node2', 'node4'], None),
        'node4': Node('node4', None, ['node5', 'node3'], None),
        'node5': Node('node5', None, ['goal', 'node6'], None),
        'goal': Node('goal' , None ,['node5'] , None),
        'node6': Node('node6', None, ['node5', 'node7'], None),
        'node7': Node('node7', None, ['node6', 'node8'], None),
        'node8': Node('node8', None, ['node7', 'node9' , 'node10'], None),
        'node9': Node('node9', None, ['node8'], None),
        'node10': Node('node10', None, ['node8', 'node11'], None),
        'node11': Node('node11', None, ['node10', 'node12' , 'node13'], None),
        'node12': Node('node12', None, ['node11', 'node14'], None),
        'node13': Node('node13', None, ['node11', 'node14'], None),
        'node14': Node('node14', None, ['node13', 'node15'], None),
        'node15': Node('node15', None, ['node14' , 'node16'], None),
        'node16': Node('node16', None, ['node15', 'node17' , 'node19'], None),
        'node17': Node('node17', None, ['node16' , 'node18'], None),
        'node18': Node('node18', None, ['node17' , 'start'], None),
        'start': Node('start', None, ['node18'], None),
        'node19': Node('node19', None, ['node16', 'node20'], None),
        'node20': Node('node20', None, ['node19' , 'node21'], None),
        'node21': Node('node21', None, ['node20' , 'node22'], None),
        'node22': Node('node22', None, ['node21' , 'node23'], None),
        'node23': Node('node23', None, ['node24' , 'node22'], None),
        'node24': Node('node24', None, ['node1' , 'node23'], None)
}

def bfs():
    initialState = 'start'
    goal = 'goal'

#     puzzle = {
#         'node1': Node('node1', None, ['node2' , 'node24'], None),
#         'node2': Node('node2', None, ['node1', 'node3'], None),
#         'node3': Node('node3', None, ['node2', 'node4'], None),
#         'node4': Node('node4', None, ['node5', 'node3'], None),
#         'node5': Node('node5', None, ['goal', 'node6'], None),
#         'goal': Node('goal' , None ,['node5'] , None),
#         'node6': Node('node6', None, ['node5', 'node7'], None),
#         'node7': Node('node7', None, ['node6', 'node8'], None),
#         'node8': Node('node8', None, ['node7', 'node9' , 'node10'], None),
#         'node9': Node('node9', None, ['node8'], None),
#         'node10': Node('node10', None, ['node8', 'node11'], None),
#         'node11': Node('node11', None, ['node10', 'node12' , 'node13'], None),
#         'node12': Node('node12', None, ['node11', 'node14'], None),
#         'node13': Node('node13', None, ['node11', 'node14'], None),
#         'node14': Node('node14', None, ['node13', 'node15'], None),
#         'node15': Node('node15', None, ['node14' , 'node16'], None),
#         'node16': Node('node16', None, ['node15', 'node17' , 'node19'], None),
#         'node17': Node('node17', None, ['node16' , 'node18'], None),
#         'node18': Node('node18', None, ['node17' , 'start'], None),
#         'start': Node('start', None, ['node18'], None),
#         'node19': Node('node19', None, ['node16', 'node20'], None),
#         'node20': Node('node20', None, ['node19' , 'node21'], None),
#         'node21': Node('node21', None, ['node20' , 'node22'], None),
#         'node22': Node('node22', None, ['node21' , 'node23'], None),
#         'node23': Node('node23', None, ['node24' , 'node22'], None),
#         'node24': Node('node24', None, ['node1' , 'node23'], None)
# }
    
    frontier = [initialState]
    explored = []
    while len(frontier)!=0:
        currentNode = frontier.pop(0)
        explored.append(currentNode)
        for child in puzzle[currentNode].actions:
            if child not in frontier and child not in explored:
                puzzle[child].parent = currentNode
                if puzzle[child].state == goal:
                    return actionSequence(puzzle , initialState , goal)
                frontier.append(child)

def actionSequence(puzzle , initialState , goal ):
    solution = [goal]
    currentParent = puzzle[goal].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = puzzle[currentParent].parent
    solution.reverse()
    return solution

import networkx as nx
import matplotlib.pyplot as plt

# ... Keep your existing Node class and BFS code ...

def visualize_puzzle(solution_path):
    G = nx.Graph()
    
    # Add nodes/edges (same as before)
    for node_name, node_data in puzzle.items():
        G.add_node(node_name)
        for neighbor in node_data.actions:
            G.add_edge(node_name, neighbor)

    # Define positions MANUALLY based on your diagram
    pos = {
        'start': (1, 0),
        'node18': (1, -1),
        'node17': (1, -2),
        'node16': (1, -3),
        'node19': (0, -3),
        'node20': (-1, -3),
        'node21': (-1, -2.4),
        'node22': (-1, -1.6),
        'node23': (-1, -0.8),
        'node24': (-1, 0.058),
        'node1': (-1, 1),
        'node2': (-0.4, 1),
        'node3': (0.2, 1),
        'node4': (1, 1),
        'node5': (2, 1),
        'goal': (2, 2),
        'node6': (2.6, 1),
        'node7': (2.5, 0.1),
        'node8': (2.5, -0.44),
        'node9': (1.7, -0.48),
        'node10': (2.5, -1),
        'node11': (2.5, -1.7),
        'node12': (1.9, -1.66),
        'node13': (2.5, -3),
        'node14': (2, -3),
        'node15': (1.5, -3),
    }
    
    # Draw nodes and edges with fixed positions
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=8)

    # Highlight solution path
    nx.draw_networkx_nodes(G, pos, nodelist=solution_path, node_color='salmon')
    path_edges = list(zip(solution_path[:-1], solution_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title("Puzzle Solution Path (BFS)")
    plt.axis("off")
    plt.show()

# Run BFS and visualize
solution = bfs()
print("Solution Path:", solution)
visualize_puzzle(solution)