# 시간의 초를 입력 받아 분과 초를 출력하는 실행 결과가 나오도록 출력
total = int(input('시간의 전체 초 입력:'))
min = total // 60
sec = total % 60
print('%d초: %d분 %d초' % (total, min, sec))
