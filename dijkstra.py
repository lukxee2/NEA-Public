def Dijkstra(edges, source, dest):
    inf = float('inf')
    distance = {}
    done = {}
    pred = {}
    for i in edges:
        distance[i] = inf
        done[i] = False
        pred[i] = 0
    distance[source] = 0
    for i in edges:
        minDist = inf; closest = None
        for j in edges:
            if not done[j]:
                if distance[j] <= minDist:
                    minDist = distance[j]
                    closest = j
        done[closest] = True
        if closest == dest:
            break
        neighbors = edge_from(closest, edges)
        for nb in neighbors:
            w = neighbors[nb]
            if not done[nb]:
                if distance[closest] + w < distance[nb]:
                    distance[nb] = distance[closest] + w
                    pred[nb] = closest
    i = dest
    if distance[i] < inf:
        thePath = i
        place = i
        while place != source:
            place = pred[place]
            if place != source:
                thePath = place + ' -> ' + thePath
        thePath = place + ' -> ' + thePath
        #print("Distance from " + str(source) + "-->" + str(dest) + " : " + str(distance[i]) + ' (' + str(thePath) + ')')
        return distance[i], thePath
    else:
        print("No path")
        return "No path"

# After further inspection, seems like I can't delete the edges variable so instead everything from this point should be ran on a thread with the output being stored in a variable.
def make_edge(from_place, to_place, length):
    def add_edge(from_place, to_place):
        if from_place not in edges:
            edges[from_place] = {}
        edges[from_place][to_place] = length
    add_edge(from_place, to_place)
    add_edge(to_place, from_place)

def make_edges(start, *args):
    for i in range(1, len(args), 2):
        make_edge(start, args[i-1], args[i])

def edge_from(place, edges):
    found = edges.get(place, None)
    if found is None:
        print("No place named '{}' found.".format(place))
    else:
        return found
    
def shortestPath(items, startPoint, order):
    #path = "" # could be this, don't even know anymore
    while items:
        minDist = 100
        ClosestItem = None
        for item in items:
            x, path = Dijkstra(edges, startPoint, item)
            if x < minDist:
                minDist, path = Dijkstra(edges, startPoint, item)
                ClosestItem = item
        startPoint = ClosestItem
        order[startPoint] = minDist
        items.remove(ClosestItem)
    return order, path

#edges = {} # Delete this and add edges to the functions so we can have multiple graphs at once.
"""TASK: Build 6 different graphs to simulate the left right, and center stairs in the floor plan.
        Each stairs should have 2 different end nodes, the left should have itself and the right, the right should have itself and the left, and the center should have the left and right.
        These tasks should be ran on python threads to speed up the processing time when rendering out the housekeeping page.
        
    AFTER CHECKING:
        Seems like there's no end node calculated for the shortest path meaning we will only need to create 3 graphs, one for each stair.
        These graphs should still be ran on different threads to speed up processing time.
"""
# The program fixes itself when you assign items to a variable after the function has started running. e.g. items = ["node2"] on line 92.
def run_left_stairs(items):
    global edges
    edges = {}
    startPoint = "start"
    order = {"start":0}
    items=list(items)
    make_edges("start", "node8", 0) # The start node has no cost to the overall travel time.
    make_edges("node8", "node7", 1)
    make_edges("node7", "node6", 1.5, "node9", 2)
    make_edges("node6", "node5", 1.5)
    make_edges("node5", "node4", 0.5, "node3", 0.5)
    make_edges("node4", "node3", 0.5)
    make_edges("node3", "node2", 0.5)
    make_edges("node2", "node1", 0.5)
    
    make_edges("node9", "node10", 1)
    make_edges("node10", "node11", 1.5)
    make_edges("node11", "node12", 1.5)
    make_edges("node12", "node13", 3)
    
    make_edges("node13", "node14", 0.5, "node17", 2) # Connect to node 17 for right side of the building (up).
    make_edges("node14", "node15", 1)
    make_edges("node15", "node16", 1.5)
    
    make_edges("node17", "node18", 2)
    make_edges("node18", "node19", 2)
    make_edges("node19", "node20", 1)
    distances, path = shortestPath(items, startPoint, order)
    z = path.split(" -> ")
    #noprint(path)
    #print(sum(distances.values()))de
    return distances, z
    
def run_right_stairs(items):
    global edges
    edges = {}
    startPoint = "start"
    order = {"start":0}
    items=list(items)
    make_edges("node8", "node7", 1)
    make_edges("node7", "node6", 1.5, "node9", 2)
    make_edges("node6", "node5", 1.5)
    make_edges("node5", "node4", 0.5, "node3", 0.5)
    make_edges("node4", "node3", 0.5)
    make_edges("node3", "node2", 0.5)
    make_edges("node2", "node1", 0.5)
    
    make_edges("node9", "node10", 1)
    make_edges("node10", "node11", 1.5)
    make_edges("node11", "node12", 1.5)
    make_edges("node12", "node13", 3)
    
    make_edges("node13", "node14", 0.5, "node17", 2) # Connect to node 17 for right side of the building (up).
    make_edges("node14", "node15", 1)
    make_edges("node15", "node16", 1.5)
    
    make_edges("node17", "node18", 2)
    make_edges("node18", "node19", 2)
    make_edges("node19", "node20", 1)
    make_edges("node20", "start", 0) # The start node has no cost to the overall travel time.
    distances, path = shortestPath(items, startPoint, order)
    z = path.split(" -> ")
    #noprint(path)
    #print(sum(distances.values()))de
    return distances, z
    
def run_central_stairs(items):
    global edges
    edges = {}
    startPoint = "start"
    order = {"start":0}
    items=list(items)
    make_edges("node8", "node7", 1)
    make_edges("node7", "node6", 1.5, "node9", 2)
    make_edges("node6", "node5", 1.5)
    make_edges("node5", "node4", 0.5, "node3", 0.5)
    make_edges("node4", "node3", 0.5)
    make_edges("node3", "node2", 0.5)
    make_edges("node2", "node1", 0.5)
    
    make_edges("node9", "node10", 1)
    make_edges("node10", "node11", 1.5)
    make_edges("node11", "node12", 1.5, "start", 1) # IN THIS CASE: The start node has a cost of 1 to the overall travel time due to the distance from the 11th node.
    make_edges("node12", "node13", 3)
    
    make_edges("node13", "node14", 0.5, "node17", 2) # Connect to node 17 for right side of the building (up).
    make_edges("node14", "node15", 1)
    make_edges("node15", "node16", 1.5)
    
    make_edges("node17", "node18", 2)
    make_edges("node18", "node19", 2)
    make_edges("node19", "node20", 1)
    distances, path = shortestPath(items, startPoint, order)
    z = path.split(" -> ")
    #noprint(path)
    #print(sum(distances.values()))de
    return distances, z