n,m,v = list(map(int,input().split()))
graph={}
for i in range(n):
    graph[i+1]=list()

for i in range(m):
    start,end = list(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)

for i in range(n):
    graph[i+1].sort()

visited = set()
def dfs(graph,v):
    global visited
    print(v,end=' ')
    visited.add(v)
    for adj in graph[v]:
        if adj not in visited:
            dfs(graph,adj)


def bfs(graph,v):
    global visited
    queue = []
    queue.append(v)
    visited.add(v)
    while queue:
        cur = queue.pop(0)
        print(cur,end=' ')
        for adj in graph[cur]:
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)

dfs(graph,v)
print()
visited.clear()
bfs(graph,v)