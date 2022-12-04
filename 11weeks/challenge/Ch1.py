# 텍스트 파일에 이름, 중간고사, 기말고사 점수가 한 라인에 존재한다고 가정했을 때,
# 실행결과를 참고하여 학생의 이름, 합계, 평균이 출력되도록 빈 곳에 알맞은 코드를 채우시오.
f = open('score1.txt')
print('이름, 합계, 평균')
for line in f:
    # split() 안에 입력안하면 공백으로 구분하여 출력
    name, mid, final = line.split()
    hap = int(mid) + int(final)
    avg = hap / 2
    print(name, hap, avg)
f.close()
