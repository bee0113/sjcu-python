# 수강하는 과목의 점수를 리스트에 저장하고
# 점수가 70점 이상인 과목의 수를 출력하는 프로그램
# len(score) -> 리스트 length 구하기
score = [70, 90, 60, 100, 50]
cnt = 0
for i in range(len(score)):
    if score[i] >= 70:
        cnt += 1
print('count:', cnt)
