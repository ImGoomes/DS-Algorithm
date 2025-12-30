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
    graphs["start"]["a"] = 10 
    
    graphs["a"] = {}
    graphs["a"]["c"] = 20

    graphs["c"] = {}
    graphs["c"]["b"] = 1
    graphs["c"]["end"] = 30

    graphs["b"] = {}
    graphs["b"]["a"] = 1

    graphs["end"] = {}

    infinit = float("inf")
    costs = {}
    costs["a"] = 10
    costs["b"] = infinit
    costs["c"] = infinit
    costs["d"] = infinit
    costs["end"] = infinit

    parent = {}
    parent["a"] = "start"
    parent["b"] = None
    parent["c"] = None
    parent["d"] = None
    parent["end"] = None
    
    dijkstra(graphs, costs, parent)
    print(f"Shortest cost to end: {costs['end']}")

main()