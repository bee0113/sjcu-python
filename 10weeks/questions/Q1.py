# 점수를 입력하면 학점을 출력해주는 함수를 정의하고 호출하기
# <학점조건>
# 90점이상이면 ‘A’
# 80점이상이면 ‘B’
# 70점이상이면 ‘C’
# 나머진 ‘F’

# ** 함수는 무조건 제일 상단에 정의해야함 **

# 함수정의
def grade(s):
    if s >= 90:
        print('A')
    elif s >= 80:
        print('B')
    elif s >= 70:
        print('C')
    else:
        print('F')


# 메인코드
score = int(input('score: '))
grade(score)
