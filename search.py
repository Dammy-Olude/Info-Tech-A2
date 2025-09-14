from my_queue import Queue
from my_stack import Stack
import networkx as nx
import matplotlib.pyplot as plt

def BFS(graph, root):
    """
    Performs a Breadth-First Search on a given graph
    to output a spanning subgraph of the original graph,
	and the sequence of nodes are visited.
    """
    #Your code here
    Nmap = graph
    Nmap.add_node(root) #this add root as the starting point
    visited = [] #this list keeps the way the nodes are visited
    q = Queue() # initializing the Queue
    q.push(root)  # adds the root nodes to the starting point

    while not q.is_empty(): #loops until there is no nodes in the queue
        temp = q.pop()  #takes the first node from the queue
        if temp not in visited:
            visited.append(temp) #marks this node as visited
            for temp2 in graph.neighbors(temp): # graph.neighbors(temp) gives all nodes with an edge to temp
                if temp2 not in visited and temp2 not in q: #check that this neighbour has not already been visited
                    Nmap.add_edge(temp,temp2) #this add the edge to the dfs spanning tree
                    q.push(temp2) #adds the neighbour into the queue



    print("BFS visited order starting from", root, ":", visited)
    return Nmap, visited



def DFS(graph, root):
    """
    Performs a Depth-First Search on a given graph starting
	from root node to output a spanning subgraph of the
	original graph, the sequence of visited nodes.
    """


    #Your code here

    Nmap = graph
    Nmap.add_node(root)  # this add root as the starting point
    visited = []  # this list keeps the way the nodes are visited
    s = Stack()  # initializing the Stack
    s.push(root)  # adds the root nodes to the starting point

    while not s.is_empty():  # loops until there is no nodes in the Stack
        temp = s.pop()  # takes the first node from the Stack
        if temp not in visited:
            visited.append(temp)  # marks this node as visited
            for temp2 in graph.neighbors(temp):  # graph.neighbors(temp) gives all nodes with an edge to temp
                if temp2 not in visited and temp2 not in s:  # check that this neighbour has not already been visited
                    Nmap.add_edge(temp, temp2)  # this add the edge to the dfs spanning tree
                    s.push(temp2)  # adds the neighbour into the stack

    print("DFS visited order starting from", root, ":", visited)
    return Nmap, visited




def show_graph(graph):
    plt.subplot(111)
    pos = nx.spring_layout(graph, seed=11)
    nx.draw(graph, with_labels=True, font_weight='bold', pos=pos)
    plt.show()

def create_tree():
    g = nx.Graph()
    for i in range(7):
        source = i if i != 3 else 0
        g.add_edge(source, i+1)
    return g

graph = nx.erdos_renyi_graph(12, 0.25, seed=42)

show_graph(graph)
BFSspan, BFSseq = BFS(graph, 0)
DFSspan, DFSseq = DFS(graph, 0)

print ("BFS Seguence: ", BFSseq)
print ("DFS Seguence: ", DFSseq)
show_graph(graph)

graph =  create_tree()
show_graph(graph)
BFSspan, BFSseq = BFS(graph, 0)
DFSspan, DFSseq = DFS(graph, 0)

print ("BFS Seguence: ", BFSseq)
print ("DFS Seguence: ", DFSseq)
show_graph(graph)
