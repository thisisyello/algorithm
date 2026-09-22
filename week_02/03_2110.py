'''
문제 설명
집 N개가 수직선 위에 있습니다.
각 집의 좌표가 주어지고, 이 중 C개의 집에 공유기를 하나씩 설치하려고 합니다.
공유기끼리는 최대한 멀리 떨어뜨리고 싶습니다.
즉, 공유기 사이의 거리 중 가장 가까운 두 공유기 사이의 거리를 최대한 크게 만들려고 합니다.
그 최댓값을 구하세요.

입력
첫째 줄에 집의 수 N과 공유기의 수 C가 주어집니다.
이후 N개의 줄에 각 집의 좌표가 하나씩 주어집니다.

입력 예시
5 3
1
2
8
4
9

제한
2 ≤ N ≤ 200,000
2 ≤ C ≤ N
집의 좌표 ≤ 1,000,000,000

출력
가장 인접한 두 공유기 사이의 거리의 최댓값을 출력합니다.

출력 예시
3
'''

import sys
input = sys.stdin.readline

homes = []
n, c = map(int, input().split())

for i in range(n):
    home = int(input())
    homes.append(home)

homes.sort()

left = 1
right = homes[-1] - homes[0]
answer = 0

while left <= right:
    mid = (left + right) // 2

    installed = 1
    last_home = homes[0]

    for home in homes[1:]:
        if home - last_home >= mid:
            installed += 1
            last_home = home

    if installed >= c:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
