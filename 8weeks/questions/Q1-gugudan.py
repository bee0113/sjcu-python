# 사용자로부터 단을 입력 받아 구국단을 출력하기
dan = int(input('단 입력:'))
for i in range(1, 10):
    print('%d*%d=%d' % (dan, i, dan * i))
