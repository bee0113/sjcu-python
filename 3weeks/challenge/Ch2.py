# [출제 가능]
# 이번 학기 수강하는 파이썬 과목은 성적반영비율이 아래와 같다
# (출석 : 20%, 과제 : 20%, 중간 : 30%, 기말 : 30%)
# 항목 점수를 각각 입력 받아 전체 총점을 출력하는 프로그램이다.
# 단, 출석점수와 과제점수는 소수점이 발생하지 않는다. 중간, 기말점수는 소수점이 발생할 수 있다. 전체 총점은 소수점 둘째자리까지 표시한다. 빈칸을 완성하시오.
name = input('이름: ')
attend = int(input('출석점수: '))
homework = int(input('과제점수:'))
mid = float(input('중간점수: '))
final = float(input('기말점수: '))
total = attend * 0.2 + homework * 0.2 + mid * 0.3 + final * 0.3
print('name: %s' % name)
print('total : %.2f ' % total)
