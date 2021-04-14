# 문제 2
"""

def dfs(graph, v, visited) :
    stack = []
    stack.append(v)
    while len(stack) > 0 :
        v = stack.pop()
        if not visited[v]  :
            visited[v] = True
            print(v, end=' ')
            graph[v].sort(key=lambda x: -x)
            stack.extend(graph[v])

graph = [
    [],  #0
    [2, 3, 8],#1
    [1, 7],   #2
    [1, 4, 5],#3
    [3, 5],   #4
    [3, 4],   #5
    [7],      #6
    [2, 6, 8],#7
    [1, 7]    #8
]

visited = [False] * 9
dfs(graph, 1, visited)
"""

# 문제 4
"""  
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] ==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
"""

# 문제 3
""" 

n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노트들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노트를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        #해당 노드 방문 처리
        graph[x][y] = 0
        #상하좌우 위치를 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)

"""
