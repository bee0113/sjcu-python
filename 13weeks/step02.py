# 1 matplotlib라이브러리에 속한 pyplot 모듈을 불러옴
# 2 평균기온을 저장하기 위한 리스트 생성
# 3평균기온을 리스트에 저장
# 4 평균기온 데이터는 숫자 값이 아닌 문자열이기때문에
#   값을 숫자 데이터형으로 변환
import csv
import matplotlib.pyplot as plt

f = open('2002.csv')
data = csv.reader(f)
header = next(data)
print(header)
temp = []
for row in data:
    temp.append(row[1])
temp = list(map(float, temp))
print(temp)

plt.title('Average temperature graph')
plt.plot(temp, linewidth=5)
plt.xlabel('day')
plt.ylabel('temperature')
plt.legend(['temperature'])
plt.show()
f.close()
