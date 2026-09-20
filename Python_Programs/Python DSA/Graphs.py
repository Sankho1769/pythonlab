edges = input('Enter edges as A-B B-C: ').split()
graph = {}
for edge in edges:
    a,b=edge.split('-'); graph.setdefault(a,[]).append(b); graph.setdefault(b,[]).append(a)
print('Graph:', graph)
