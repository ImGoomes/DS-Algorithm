from collections import deque

graph = {}
graph["Chico"] = ["Marcos", "Amanda", "Gustavo"]
graph["Amanda"] = []
graph["Gustavo"] = []
graph["Marcos"] = ["Alex", "Igor"]
graph["Alex"] = []
graph["Igor"] = ["Amanda", "Vinicius"] 
graph["Vinicius"] = ["Adam", "Melissa"]
graph["Adam"] = []
graph["Melissa"] = ["Gustavo"]

def is_a_seller (name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    verified = []
    
    while search_queue:
        person = search_queue.popleft();
        if not person in verified:
            if is_a_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                verified.append(person)
    
    return False

 

search("Chico")

