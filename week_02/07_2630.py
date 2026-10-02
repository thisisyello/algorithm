'''
문제 설명
정사각형 모양의 종이가 있고, 각 칸은 0 또는 1로 표시되어 있습니다.
0 = 하얀색
1 = 파란색
현재 종이가 모두 같은 색이면 하나의 색종이로 사용합니다.
하지만 색이 섞여 있다면 종이를 똑같은 크기의 4개 정사각형으로 나누고, 각 부분에 대해 같은 작업을 반복합니다.
최종적으로 만들어지는:
하얀색 색종이 개수
파란색 색종이 개수
를 구하세요.

입력
첫째 줄에 종이의 한 변의 길이 N이 주어집니다.
그다음 N개의 줄에 각 칸의 색 정보가 주어집니다.
입력 예시
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

제한
N은 2, 4, 8, 16, 32, 64, 128 중 하나

출력
첫째 줄에 하얀색 색종이의 개수를 출력합니다.
둘째 줄에 파란색 색종이의 개수를 출력합니다.
출력 예시
9
7
'''

import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def divide(row, col, size):
    global white, blue

    color = paper[row][col]
    is_same = True

    for i in range(row, row + size):
        for j in range(col, col + size):
            if paper[i][j] != color:
                is_same = False
                break
        if not is_same:
            break

    if is_same:
        if color == 0:
            white += 1
        else:
            blue += 1
        return

    half = size // 2
    divide(row, col, half)
    divide(row, col + half, half)
    divide(row + half, col, half)
    divide(row + half, col + half, half)


divide(0, 0, n)

print(white)
print(blue)
