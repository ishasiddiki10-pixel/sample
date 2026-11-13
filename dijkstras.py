INF = 99999
def printpath(parent, v):
    if v == -1:
        return
    printpath(parent, parent[v])
    print(v, end = '')
n = int(input("Enter number of vertices: "))
print("Enter Adjacency matrix")
cost = []
for _ in range(n):
    row = list(map(int, input().split()))
    cost.append(row)
src = int(input("Enter the source vertex : "))
dist = [INF]*n 
visited = [0]*n
parent =[-1]*n
dist[src] = 0
for _ in range(n - 1):
    mini = INF
    u = -1
    for i in range(n):
        if not visited[i] and dist[i] < mini:
            u = i
            mini = dist[i]
    if u == -1:
        break
    visited[u] = 1
    for j in range(n):
        if not visited[j] and cost[u][j] != 0 and dist[u] != INF and dist[u] + cost[u][j] < dist[j]:
            dist[j] = dist[u] + cost[u][j]
            parent[j] = u
print("\nShortest distances from source", src)
for i in range(n):
    print("To", i, end=": ")
    if dist[i] == INF:
        print("Unreachable")
    else:
        print(dist[i], end="\tPath: ")
        printpath(parent, i)
        print()