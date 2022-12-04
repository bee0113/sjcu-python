# 사용자로부터 두 정수를 입력 받아 덧셈 결과를 출력하는 프로그램
# 덧셈 함수의 형태 : 두 정수를 매개변수로 받아 처리한 후 결과값을 돌려주는 함수

# 함수정의
def add(n1, n2):
    result = n1 + n2
    return result


# 메인코드
num1 = int(input('num1: '))
num2 = int(input('num2: '))

# 함수호출
result = add(num1, num2)
print(result)
