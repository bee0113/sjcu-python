# 커피 메뉴가 ame, cafelattee, cafemoca 있을 때 하루에 판매 된 수량을 각각 입력 받아 총 매출액을 계산하는 프로그램을 작성하시오.
# 또한 하루 재료비가 100,000원 일 경우 순이익을 구하시오.
# - 변수명 : 아메(ame), 카페라떼(cafelattee), 카페모카(cafemoca), 총매출(total) - 가격 : ame=2,000, cafelattee=3,000, cafemoca=4,000
ame = int(input('커피수량:'))
cafelattee = int(input('라떼수량:'))
cafemoca = int(input('모카수량:'))
total = (ame * 2000) + (cafelattee * 3000) + (cafemoca * 4000)
print('total:{}'.format(total))
print('순이익:{}'.format(total - 100029000))
