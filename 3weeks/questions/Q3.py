# 가로 및 세로 길이를 입력 받아 사각형의 넓이를 계산한 후, format() 함수를 이용하여 출력
width = int(input('가로 길이:'))
height = int(input('세로 길이:'))
area = width * height
print('가로: {}, 세로: {}, 넓이: {}'.format(width, height, area))
