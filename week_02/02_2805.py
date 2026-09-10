'''
문제 설명
나무 N그루가 있고, 각 나무의 높이가 주어집니다.
절단기의 높이를 H로 설정하면, 높이가 H보다 큰 나무만 잘립니다.
예를 들어 나무 높이가:
20 15 10 17
이고 절단 높이가:
H = 15
라면 가져가는 나무 길이는:
20 → 5
15 → 0
10 → 0
17 → 2
총 7이 됩니다.
필요한 나무 길이가 M일 때, 적어도 M만큼의 나무를 가져갈 수 있는 절단기 높이 H의 최댓값을 구하세요.

입력
첫째 줄에 나무의 수 N과 필요한 나무 길이 M이 주어집니다.
둘째 줄에 나무 N개의 높이가 주어집니다.
입력 예시
4 7
20 15 10 17

제한
1 ≤ N ≤ 1,000,000
1 ≤ M ≤ 2,000,000,000
나무 높이 ≤ 1,000,000,000

출력
적어도 M만큼의 나무를 얻을 수 있는 절단기 높이의 최댓값을 출력합니다.
출력 예시
15
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

left = 0
right = max(heights)
answer = 0

while left <= right:
    mid = (left + right) // 2
    tree = 0

    for height in heights:
        if height > mid:
            tree += height - mid

    if tree >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
