import matplotlib.pyplot as plt
import networkx as nx
import math

# Node class definition
class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

def findMin(frontier):
    minV = math.inf
    node = ''
    for i in frontier:
        if minV > frontier[i][1]:
            minV = frontier[i][1]
            node = i
    return node

# Helper function to reconstruct the path
def actionSequence(puzzle, initialState, goal):
    solution = [goal]
    currentParent = puzzle[goal].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = puzzle[currentParent].parent
    solution.reverse()
    return solution

# UCS algorithm to find the optimal path
def UCS():
    initialState = 'Arad'
    goalState = 'Bucharest'
    
    romania_graph = {
        'Arad': Node('Arad', None, [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 740)], 0),
        'Zerind': Node('Zerind', None, [('Arad', 75), ('Oradea', 71)], 0),
        'Oradea': Node('Oradea', None, [('Zerind', 71), ('Sibiu', 151)], 0),
        'Timisoara': Node('Timisoara', None, [('Arad', 118), ('Lugoj', 111)], 0),
        'Lugoj': Node('Lugoj', None, [('Timisoara', 111), ('Mehadia', 70)], 0),
        'Mehadia': Node('Mehadia', None, [('Lugoj', 70), ('Drobeta', 75)], 0),
        'Drobeta': Node('Drobeta', None, [('Mehadia', 75), ('Craiova', 120)], 0),
        'Craiova': Node('Craiova', None, [('Drobeta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)], 0),
        'Rimnicu Vilcea': Node('Rimnicu Vilcea', None, [('Craiova', 146), ('Pitesti', 97), ('Sibiu', 80)], 0),
        'Sibiu': Node('Sibiu', None, [('Arad', 140), ('Oradea', 151), ('Rimnicu Vilcea', 80), ('Fagaras', 989)], 0),
        'Fagaras': Node('Fagaras', None, [('Sibiu', 99), ('Bucharest', 211)], 0),
        'Pitesti': Node('Pitesti', None, [('Craiova', 138), ('Rimnicu Vilcea', 97), ('Bucharest', 101)], 0),
        'Bucharest': Node('Bucharest', None, [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)], 0),
        'Giurgiu': Node('Giurgiu', None, [('Bucharest', 90)], 0),
        'Urziceni': Node('Urziceni', None, [('Bucharest', 85), ('Neamt', 87), ('Vaslui', 142)], 0),
        'Neamt': Node('Neamt', None, [('Urziceni', 87)], 0),
        'Vaslui': Node('Vaslui', None, [('Urziceni', 142), ('Iasi', 92)], 0),
        'Iasi': Node('Iasi', None, [('Vaslui', 92), ('Neamt', 87)], 0),
        'Hirsova': Node('Hirsova', None, [('Urziceni', 98), ('Eforie', 86)], 0),
        'Eforie': Node('Eforie', None, [('Hirsova', 86)], 0)
    }

    frontier = dict()
    frontier[initialState] = (None, 0)  # (parent, cost)
    explored = []

    while len(frontier) != 0:
        currentNode = findMin(frontier)
        del frontier[currentNode]

        if romania_graph[currentNode].state == goalState:
            return actionSequence(romania_graph, initialState, goalState)

        explored.append(currentNode)

        for child in romania_graph[currentNode].actions:
            currentCost = child[1] + (romania_graph[currentNode].totalCost if romania_graph[currentNode].totalCost is not None else 0)

            if child[0] not in frontier and child[0] not in explored:
                romania_graph[child[0]].parent = currentNode
                romania_graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (romania_graph[child[0]].parent, romania_graph[child[0]].totalCost)

            elif child[0] in frontier:
                if frontier[child[0]][1] > currentCost:
                    frontier[child[0]] = (currentNode, currentCost)
                    romania_graph[child[0]].parent = currentNode
                    romania_graph[child[0]].totalCost = currentCost

    return None  # If no path is found

# Function to visualize the Romania map with the UCS path
def visualize_romania_map():
    # Step 1: Get the path from UCS
    path = UCS()
    if not path:
        print("No path found from Arad to Bucharest!")
        return

    # Step 2: Create a graph using NetworkX
    G = nx.Graph()

    # Add nodes (cities)
    cities = [
        'Arad', 'Zerind', 'Oradea', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta',
        'Craiova', 'Rimnicu Vilcea', 'Sibiu', 'Fagaras', 'Pitesti', 'Bucharest',
        'Giurgiu', 'Urziceni', 'Neamt', 'Vaslui', 'Iasi', 'Hirsova', 'Eforie'
    ]
    G.add_nodes_from(cities)

    # Add edges with weights (costs) based on the romania_graph
    edges = [
        ('Arad', 'Zerind', 75), ('Arad', 'Timisoara', 118), ('Arad', 'Sibiu', 140),
        ('Zerind', 'Oradea', 71),
        ('Oradea', 'Sibiu', 151),
        ('Timisoara', 'Lugoj', 111),
        ('Lugoj', 'Mehadia', 70),
        ('Mehadia', 'Drobeta', 75),
        ('Drobeta', 'Craiova', 120),
        ('Craiova', 'Pitesti', 138), ('Craiova', 'Rimnicu Vilcea', 146),
        ('Rimnicu Vilcea', 'Pitesti', 97), ('Rimnicu Vilcea', 'Sibiu', 80),
        ('Sibiu', 'Fagaras', 99),
        ('Fagaras', 'Bucharest', 211),
        ('Pitesti', 'Bucharest', 101),
        ('Bucharest', 'Giurgiu', 90), ('Bucharest', 'Urziceni', 85),
        ('Urziceni', 'Neamt', 87), ('Urziceni', 'Vaslui', 142), ('Urziceni', 'Hirsova', 98),
        ('Vaslui', 'Iasi', 92),
        ('Iasi', 'Neamt', 87),
        ('Hirsova', 'Eforie', 86)
    ]
    G.add_weighted_edges_from(edges)

    # Step 3: Define approximate positions for visualization
    pos = {
        'Arad': (0, 4),
        'Zerind': (1, 5),
        'Oradea': (2, 6),
        'Timisoara': (0, 2),
        'Lugoj': (1, 1),
        'Mehadia': (1, 0),
        'Drobeta': (0, -1),
        'Craiova': (2, -1),
        'Rimnicu Vilcea': (3, 2),
        'Sibiu': (2, 3),
        'Fagaras': (4, 3),
        'Pitesti': (4, 1),
        'Bucharest': (5, 0),
        'Giurgiu': (5, -1),
        'Urziceni': (6, 1),
        'Neamt': (6, 5),
        'Vaslui': (7, 3),
        'Iasi': (7, 4),
        'Hirsova': (7, 0),
        'Eforie': (8, -1)
    }

    # Step 4: Define the path edges to highlight
    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]

    # Step 5: Visualize the graph
    plt.figure(figsize=(12, 8))

    # Draw all nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)

    # Draw all edges (default color)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1)

    # Highlight the UCS path edges in red
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    # Draw labels for nodes (cities)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    # Draw edge labels (costs)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Step 6: Add title and display the plot
    plt.title(f"Romania Map with UCS Optimal Path (Arad to Bucharest, Cost: {sum(G[u][v]['weight'] for u, v in path_edges)})", fontsize=14)
    plt.axis('off')  # Hide axes
    plt.show()

# Run the visualization with the UCS path
visualize_romania_map()