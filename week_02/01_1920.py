'''
문제 설명
N개의 정수가 주어집니다.
그 다음 M개의 정수가 주어질 때, 각각의 수가 처음 주어진 N개의 정수 안에 존재하는지 확인하세요.
존재하면 1, 존재하지 않으면 0을 출력합니다.

입력
첫째 줄에 자연수 N이 주어집니다.
둘째 줄에 N개의 정수가 주어집니다.
셋째 줄에 자연수 M이 주어집니다.
넷째 줄에 확인할 M개의 정수가 주어집니다.
입력 예시
5
4 1 5 2 3
5
1 3 7 9 5

제한
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000

출력
확인할 숫자마다 첫 번째 배열에 존재하면 1, 존재하지 않으면 0을 한 줄에 하나씩 출력합니다.
출력 예시
1
1
0
0
1
'''

import sys
input = sys.stdin.readline

n = int(input())
nums_1 = sorted(list(map(int, input().split())))
m = int(input())
nums_2 = list(map(int, input().split()))

for target in nums_2:
    left = 0
    right = len(nums_1) - 1
    found = False

    while left <= right:
        mid = (left + right) // 2

        if target == nums_1[mid]:
            found = True
            break
        elif target > nums_1[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if found:
        print(1)
    else:
        print(0)

# --------------- 오우 쮓 2분탐색으로 풀어라잉 ---------------
# for num_2 in nums_2:
#     if num_2 in nums_1:
#         print(1)
#     else:
#         print(0)
