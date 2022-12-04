# 다음은 사용자가 입력한 숫자가 홀수인지 짝수인지 판별하는 프로그램이다.
# 단, 숫자에 0을 입력하면 프로그램을 종료한다. 실행 결과가 나오도록 빈칸을 완성하시오.
while True:
    num = int(input("수를 입력: "))
    if num == 0:
        print("종료")
        break
    elif num % 2 == 0:
        print("짝수")
    else:
        print("홀수")
