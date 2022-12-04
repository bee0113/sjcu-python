# 스마트폰에서 친구를 등록하고, 친구를 이름으로 검색한 후 연락처를 출력하는 프로그램을 작성하시오. 실행결과를 참고하여 문제를 해결하시오.
# [조건]
# 1.선택메뉴: 1) 친구등록 2) 검색 3) 종료
# 2.딕셔너리 자료 구조 사용
# 3.새로운 친구를 등록함
# 4.찾는 친구가 있으면 연락처를 출력하고 없으면 에러 메시지를 출력함

addr = {}  # 빈 딕셔너리 생성
while True:
    menu = int(input("선택 메뉴: \n1)친구등록\n2)검색\n3)종료\n"))
    if menu == 1:
        name = input("이름:")
        phone = input("전화번호:")
        # addr[key] = value
        addr[name] = phone
    elif menu == 2:
        name = input('검색할 친구 이름:')
        print(addr.get(name, '찾는 친구가 없습니다.'))
    elif menu == 3:
        print("종료합니다.")
        break
    else:
        print("없는 메뉴 입니다.")
