'''
문제 설명
N개의 용액이 있고, 각 용액에는 하나의 정수가 주어집니다.
두 용액을 섞었을 때의 특성값은 두 수의 합입니다.
두 용액을 골라서 합이 0에 가장 가까운 두 용액을 찾으세요.
예를 들어:
-99 -2 -1 4 98
이라면 -99 + 98 = -1이므로 0에 가장 가깝습니다.

입력
첫째 줄에 용액의 수 N이 주어집니다.
둘째 줄에 N개의 용액 특성값이 공백으로 구분되어 주어집니다.
입력 예시
5
-2 4 -99 -1 98

제한
2 ≤ N ≤ 100,000
각 용액의 특성값의 절댓값 ≤ 1,000,000,000

출력
합이 0에 가장 가까운 두 용액의 특성값을 오름차순으로 출력합니다.
출력 예시
-99 98
'''

import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = n - 1
best_sum = float("inf")
answer = (liquid[left], liquid[right])

while left < right:
    current_sum = liquid[left] + liquid[right]

    if abs(current_sum) < abs(best_sum):
        best_sum = current_sum
        answer = (liquid[left], liquid[right])

    if current_sum < 0:
        left += 1
    elif current_sum > 0:
        right -= 1
    else:
        break

print(*answer)
