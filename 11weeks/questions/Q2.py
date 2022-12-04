# 텍스트 파일 저장과 읽기
# 우리 과 졸업 전시회에 참석한 학생들의 이름을 입력 받아 ‘welcome’을 출력하고,
# 참석한 명단을 guest.txt 파일에 저장한 뒤,
# guest.txt 파일을 읽어서 전시회에 참석한 학생의 총 인원수를 출력하는 프로그램

f = open('guest.txt', 'w')
while True:
    name = input('name : ')
    if not name:
        break
    print('{} welecome!!'.format(name))
    f.write(name + '\n')
f.close()

f = open('guest.txt')
lines = f.readlines()
cnt = len(lines)
print('total count : {}'.format(cnt))
