# 성적파일(score2.txt)에 학생이름과 성적이 저장되었을 때
# 성적파일을 읽어서 학생의 이름과 성적에 대한 학점을 계산하여 화면에 출력하는 프로그램을 완성하시오.
def grade(s):
    if s >= 90:
        result = 'A'
    elif s >= 80:
        result = 'B'
    elif s >= 70:
        result = 'C'
    else:
        result = 'F'

    return result


f = open('score2.txt')
print('이름, 평균, 학점')
for line in f:
    name, avg = line.split()
    avg = int(avg)
    res = grade(avg)
    print(name, avg, res)
f.close()
