# 다음은 행운의 로또 복권 프로그램의 일부분이다.
# 로또 번호는 1~45숫자 중 총 6개의 숫자로 구성된다. 빈칸을 완성하시오.
import random

lotto = []  # 빈 리스트 생성
print('로또 프로그램 시작')
while True:
    num = random.randint(1, 45)
    # 중복된 숫자 제거
    if lotto.count(num) == 0:
        lotto.append(num)  # 리스트 추가

    if len(lotto) == 6:
        break

print('추첨된 로또 번호')
lotto.sort()

for i in range(6):
    print('{}'.format(lotto[i]), end=' ')
