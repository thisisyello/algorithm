'''
문제 설명
어떤 지역의 높이 정보가 N x N 크기의 격자로 주어집니다.
비가 일정 높이만큼 내리면, 그 높이 이하의 지역은 물에 잠깁니다.
물에 잠기지 않은 지역들 중에서 상하좌우로 서로 연결된 영역을 하나의 안전 영역이라고 합니다.
비의 높이를 여러 값으로 바꿔가면서 확인했을 때, 안전 영역의 개수가 최대 몇 개인지 구하세요.

입력
첫째 줄에 지역의 크기 N이 주어집니다.
이후 N개의 줄에 각 지역의 높이가 주어집니다.
예시:
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

제한
2 ≤ N ≤ 100
각 지역의 높이 ≤ 100

출력
안전 영역의 최대 개수를 출력합니다.
예시:
5
'''

import sys
input = sys.stdin.readline


n = int(input())
heights = []

for _ in range(n):
    heights.append(list(map(int, input().split())))

max_height = max(max(row) for row in heights)
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# --------------- 스택을 사용한 반복문 DFS 풀이 ---------------
# for rain in range(max_height + 1):
#     visited = [[False] * n for _ in range(n)]
#     count = 0

#     for i in range(n):
#         for j in range(n):
#             if heights[i][j] > rain and not visited[i][j]:
#                 stack = [(i, j)]
#                 visited[i][j] = True

#                 while stack:
#                     x, y = stack.pop()

#                     for direction in range(4):
#                         nx = x + dx[direction]
#                         ny = y + dy[direction]

#                         if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                             continue

#                         if visited[nx][ny]:
#                             continue

#                         if heights[nx][ny] <= rain:
#                             continue

#                         visited[nx][ny] = True
#                         stack.append((nx, ny))

#                 count += 1

#     if answer < count:
#         answer = count

# print(answer)

# --------------- 재귀 dfs()를 이용한 풀이 ---------------
def dfs(x, y, rain, visited):
    visited[x][y] = True

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if visited[nx][ny]:
            continue

        if heights[nx][ny] <= rain:
            continue

        dfs(nx, ny, rain, visited)


for rain in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if heights[i][j] > rain and not visited[i][j]:
                dfs(i, j, rain, visited)
                count += 1

    if answer < count:
        answer = count

print(answer)
