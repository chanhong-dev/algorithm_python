# https://ebbnflow.tistory.com/173

N, M, V = map(int, input().split())
matrix = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list = [0]*(N+1)


def dfs(v):
    visit_list[v] = 1
    print(v, end=' ')
    for i in range(1, N+1):
        if visit_list[i] == 0 and matrix[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit_list[v] = 0
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):
            if visit_list[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visit_list[i] = 0


dfs(V)
print()
bfs(V)
