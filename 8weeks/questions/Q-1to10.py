# 1~10 출력
print('*' * 30)
print('1~10 출력 for문')
for i in range(1, 11):
    print(i, end=' ')
print()

print('*' * 30)
print('1~10 출력 while문')
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
print()

# 10~1
print('*' * 30)
print('10~1 출력 for문')
for i in range(10, 0, -1):
    print(i, end=' ')
print()

print('*' * 30)
print('10~1 출력2 for문')
for i in reversed(range(1,11)):
    print(i, end=' ')
print()

print('*' * 30)
print('10~1 출력 while문')
i = 10
while i >= 1:
    print(i, end=' ')
    i -= 1
print()
