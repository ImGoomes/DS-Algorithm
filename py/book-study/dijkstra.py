processed = []
   
def dijkstra(graphs, costs, parent):
    node = node_with_lowest_cost(costs)
    while node is not None: 
        cost = costs[node]
        neighbor = graphs[node]
        for n in neighbor.keys():
            new_cost = cost + neighbor[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parent[n] = node
        processed.append(node)
        node = node_with_lowest_cost(costs)

def node_with_lowest_cost(costs):
    lowest_cost = float("inf")
    node_with_lowest_cost = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            node_with_lowest_cost = node
    return node_with_lowest_cost

def main(): 
    graphs = {}
    graphs["start"] = {}
    graphs["start"]["a"] = 5 
    graphs["start"]["b"] = 2
    
    graphs["a"] = {}
    graphs["a"]["c"] = 4
    graphs["a"]["d"] = 2
    
    graphs["b"] = {}
    graphs["b"]["a"] = 8
    graphs["b"]["d"] = 7

    graphs["c"] = {}
    graphs["c"]["end"] = 3
    graphs["c"]["d"] = 6

    graphs["d"] = {}
    graphs["d"]["end"] = 1

    graphs["end"] = {}

    infinit = float("inf")
    costs = {}
    costs["a"] = 5
    costs["b"] = 2
    costs["c"] = infinit
    costs["d"] = infinit
    costs["end"] = infinit

    parent = {}
    parent["a"] = "start"
    parent["b"] = "start"
    parent["c"] = None
    parent["d"] = None
    parent["end"] = None
    
    dijkstra(graphs, costs, parent)
    print(f"Shortest cost to end: {costs['end']}")

main()