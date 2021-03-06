# 딴놈풀이
def score_3(a, b, c):  # 3자리씩 끊어 읽기
    if a == b == c:  # 모든 숫자가 같음
        return 1
    if a - b == b - c == 1 or a - b == b - c == -1:  # 단조증가/감소
        return 2
    if a == c != b:  # 숫자가 번갈아 출현
        return 4
    if a - b == b - c:  # 등차수열
        return 5
    return 10


def score_4(a, b, c, d):  # 4자리씩 끊어 읽기
    if a == b == c == d:
        return 1
    if a - b == b - c == c - d == 1 or a - b == b - c == c - d == -1:
        return 2
    if a == c and b == d and a != b:
        return 4
    if a - b == b - c == c - d:
        return 5
    return 10


def score_5(a, b, c, d, e):  # 5자리씩 끊어 읽기
    if a == b == c == d == e:
        return 1
    if a - b == b - c == c - d == d - e == 1 or a - b == b - c == c - d == d - e == -1:
        return 2
    if a == c == e and b == d and a != b:
        return 4
    if a - b == b - c == c - d == d - e:
        return 5
    return 10


def pi(arr):
    N = len(arr)  # 리스트의 길이
    cache = [None] * (N + 1)
    cache[3] = score_3(arr[0], arr[1], arr[2])  # 0~2번까지 3개 읽음
    cache[4] = score_4(arr[0], arr[1], arr[2], arr[3])  # 0~3번까지 4개 읽음
    cache[5] = score_5(arr[0], arr[1], arr[2], arr[3], arr[4])  # 0~4번까지 5개 읽음
    for i in range(6, N + 1):
        cand = []
        if cache[i - 3] is not None:
            cand.append(cache[i - 3] + score_3(arr[i - 3], arr[i - 2], arr[i - 1]))
        if cache[i - 4] is not None:
            cand.append(cache[i - 4] + score_4(arr[i - 4], arr[i - 3], arr[i - 2], arr[i - 1]))
        if cache[i - 5] is not None:
            cand.append(cache[i - 5] + score_5(arr[i - 5], arr[i - 4], arr[i - 3], arr[i - 2], arr[i - 1]))
        cache[i] = min(cand)  # 최소값을 cache에 넣는다
    return cache[-1]


case = int(input())
for k in range(case):
    number = list(map(int, list(input().strip())))  # 입력을 숫자 리스트로 만든다
    print(pi(number))
