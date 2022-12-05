# n, step, hap = 3, 0, 5
# while step <= n:
#     hap += step
#     step += 1
# print(hap)
#
# hap = 2
# for num in range(5):
#     hap += num
# print(hap)
#
# i = 10
# while i >= 1:
#     print(i, end=' ')
#     i =i-1

# 딕셔너리
# menu = {'쌀국수': 4500, '볶음우동': 5000, '햄버거': 4000}
# for k in menu.keys():
#     print(k, ':', menu[k])

# while True:
#     point = int(input('포인트입력:'))
#     if point == 0:
#         break
#     num = point // 10
#     for i in range(num):
#         print('@', end="")
#     print()

# score=[70,90,60,100,50]
# cnt=0
# for i in range(5):
#     if score[i]<=60:
#         cnt+=1
# print('cnt',cnt)

def hap(a, b):
    result = 0
    for i in range(a, b + 1):
        result += i
    return result


s = int(input('시작: '))
e = int(input('종료: '))
print(hap(s, e))
