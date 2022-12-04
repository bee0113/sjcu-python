# 사각형 그리기 - 효율적으로 그리기
# <알고리즘>
# 사각형 그리는 동작은 -앞으로일정거리이동 -왼쪽또는오른쪽으로90도회전과정 을 4번 반복하면 된다.
# <반복문 사용>
from turtle import *

shape('turtle')
for i in range(4):
    forward(100)
    left(90)
