# 1부터 사용자로부터 입력 받은 숫자까지 짝수/홀수 판별하는 프로그램

n = int(input('수를 입력:'))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, '짝수')
    else:
        print(i, '홀수')

# 1~100까지
for i in range(1, 101):
    print(i, end=" ")
