# 다음은 사용자가 입력한 숫자와 컴퓨터가 생각한 숫자가 일치하는 지를 판단하는 숫자 UP/DOWN 게임이다.
# 실행 결과가 나오도록 빈 곳을 완성하시오.

import random

com = random.randint(1, 20)
print("<<컴퓨터가 생각하는 1~20 숫자 맞추기>>")
# print("난수 %d" % com)
while True:
    player = int(input("숫자 입력(종료 0): "))
    if (player == 0):
        print("종료")
        break
    elif (player == com):
        print("%d 정답!!" % com)
        break
    elif (player > com):
        print("더 작은 숫자 입력!")
        continue
    else:
        print("더 큰 숫자 입력!")
        continue
