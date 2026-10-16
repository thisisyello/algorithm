'''
문제 설명
자연수 A, B, C가 주어집니다.
다음 값을 구하세요.
A^B mod C
즉, A를 B번 곱한 값을 C로 나눈 나머지를 구하는 문제입니다.

입력
첫째 줄에 A, B, C가 공백으로 구분되어 주어집니다.
입력 예시
10 11 12

제한
1 ≤ A, B, C ≤ 2,147,483,647

출력
A^B를 C로 나눈 나머지를 출력합니다.
출력 예시
4
'''

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())


def power(x, y):
    if y == 0:
        return 1

    half = power(x, y // 2)
    answer = (half * half) % c

    if y % 2 != 0:
        answer = (answer * x) % c

    return answer

print(power(a, b))