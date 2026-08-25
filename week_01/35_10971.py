'''
문제 설명
N개의 도시가 있고, 각 도시 사이를 이동하는 비용이 주어집니다.
한 도시에서 출발해서 모든 도시를 한 번씩 방문한 뒤 다시 출발 도시로 돌아오는 여행 경로를 만들려고 합니다.
가능한 경로 중에서 이동 비용의 합이 가장 작은 값을 구하세요.

입력
첫째 줄에 도시의 수 N이 주어집니다.
둘째 줄부터 N개의 줄에 걸쳐 비용 행렬이 주어집니다.
W[i][j]는 i번 도시에서 j번 도시로 이동하는 비용입니다.
예시:
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0

제한
2 ≤ N ≤ 10
0 ≤ W[i][j] ≤ 1,000,000
W[i][j] = 0 이면 i → j로 갈 수 없음

출력
가능한 순회 경로 중 최소 비용을 출력합니다.
예시:
35
'''

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
w = []

for _ in range(n):
    w.append(list(map(int, input().split())))

answer = float("inf")

for route in permutations(range(n)):
    total = 0
    possible = True

    for i in range(n - 1):
        start = route[i]
        end = route[i + 1]

        if w[start][end] == 0:
            possible = False
            break

        total += w[start][end]

    if not possible:
        continue

    if w[route[-1]][route[0]] == 0:
        continue

    total += w[route[-1]][route[0]]
    answer = min(answer, total)

print(answer)
