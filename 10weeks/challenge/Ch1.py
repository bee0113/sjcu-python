# 다음 실행결과를 보고 파이썬 코드의 빈 칸에 알맞은 코드를 채우시오.

def greet(lang):
    if lang == 1:
        print('Hello')
    elif lang == 2:
        print('Bonjour')
    elif lang == 3:
        print('안녕?')
    else:
        print('지원하지 않습니다')


h = int(input('언어를 선택하세요(1:EN/2:FR/3:KR)'))
greet(h)
