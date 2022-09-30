# 두 정수를 입력받고, 사칙연산자 중 하나를 입력받아 사칙연산의 결과를 출력한다
num1 = int(input('num1:'))
num2 = int(input('num2:'))
op = input("연산 기호:(+-*/)")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
else:
    result = num1 / num2

print('%d %s %d = %.1f' % (num1, op, num2, result))
