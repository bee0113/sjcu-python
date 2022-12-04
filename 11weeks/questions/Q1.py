# 텍스트 파일의 내용을 모두 읽어 화면에 출력

f = open('data1.txt')
lines = f.read()
print(lines)
f.close()

# with구문동일한결과
with open('data1.txt') as f:
    lines = f.read()
    print(lines)
