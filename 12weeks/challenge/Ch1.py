# 터틀 그래픽 모듈이 제공하는 함수를 이용하여 입력 받은 숫자에 따라 다각형을 그리는 프로그램이다.
# 빈 곳에 알맞은 코드를 채우시오.
from turtle import *


def makepolygon(n):
    for i in range(n):
        forward(100)
        left(360 / n)


shape('turtle')
n = int(textinput('도형그리기', '숫자입력(삼각형:3,사각형:4,오각형:5):'))
if n in [3, 4, 5]:
    makepolygon(n)
else:
    print('error')
