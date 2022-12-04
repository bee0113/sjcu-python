# 1 csv 모듈을 불러옴
# 2 csv 파일을 open() 함수를 열어서 f에 저장함
# 3 csv 파일에서 데이터를 읽어와서 data에 저장함
# 4 header라는 변수에 헤더 데이터 행을 저장함
# 5 header를 출력함
# 6 데이터를 한 줄씩 읽어와서
# 7 화면에 출력
import csv

f = open('2002.csv')
data = csv.reader(f)
header = next(data)
print(header)
for row in data:
    print(row)
f.close()
