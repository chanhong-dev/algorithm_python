n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

visited = []


def dfs(graph, v, visited):
    print(v, end=' ')
    visited.append(v)
    for adjacent_node in graph[v]:
        if adjacent_node not in visited:
            dfs(graph, adjacent_node, visited)
    return


def bfs(adj_graph, start_node):
    queue = [start_node]
    visited = []
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        print(current_node, end=' ')
        for adj_node in adj_graph[current_node]:
            if adj_node not in visited:
                queue.append(adj_node)
                visited.append(adj_node)

    return visited


dfs(graph, v, visited)
print()
bfs(graph, v)
