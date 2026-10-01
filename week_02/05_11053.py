'''
문제 설명
수열 A가 주어집니다.
이 수열에서 몇 개의 숫자를 골라 앞에서 뒤로 갈수록 값이 계속 증가하도록 만들려고 합니다.
그렇게 만들 수 있는 부분 수열 중 가장 긴 길이를 구하세요.
예를 들어:
10 20 10 30 20 50
에서는:
10 → 20 → 30 → 50
처럼 길이 4인 증가하는 부분 수열을 만들 수 있습니다.
중요한 점은 연속된 숫자일 필요는 없지만 원래 순서는 유지해야 한다는 것입니다.

입력
첫째 줄에 수열의 크기 N이 주어집니다.
둘째 줄에 N개의 수가 주어집니다.
입력 예시
6
10 20 10 30 20 50

제한
1 ≤ N ≤ 1,000
1 ≤ A[i] ≤ 1,000

출력
가장 긴 증가하는 부분 수열의 길이를 출력합니다.
출력 예시
4
'''

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

tails = []

for number in a:
    index = bisect_left(tails, number)

    if index == len(tails):
        tails.append(number)
    else:
        tails[index] = number

print(len(tails))
