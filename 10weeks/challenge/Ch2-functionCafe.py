# - 가격 : 아메리카노 2500원, 카페라떼 3000원, 바닐라라떼 3000원
# - 메뉴번호를 선택하면 해당메뉴와 가격을 출력해 주는 부분을 함수로 작성

def price(menu):
    if menu == 1:
        m = '아메리카노'
        p = '2500원'
    elif menu == 2:
        m = '카페라떼'
        p = '3000원'
        print('카페라떼 3000원')
    elif menu == 3:
        m = '바닐라라떼'
        p = '3000원'

    print(m, p, end=' ')


# 메인코드
m = int(input('메뉴선택(1:아메리카노/2:카페라떼/3:바닐라라떼)'))
# 함수호출
price(m)
