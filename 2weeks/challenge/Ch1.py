# 조건: 변수에 정수 396을 저장한 후, 백의자리, 십의자리,일의자리로 분리
# 예 : 정수 123인 경우 백의자리 1, 십의자리 2, 일의자리 3의 결과를 출력
# Hint :  몫(//), 나머지(%) 연산자 활용
n = 396
d100 = n // 100
n = n % 100
d10 = n // 10
d1 = n % 10

print('백의자리 ', d100)
print('십의자리 ', d10)
print('일의자리 ', d1)