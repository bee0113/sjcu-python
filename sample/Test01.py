testList = [1, 2, 3, 4, 5]
testList = list(map(lambda num: num + 100, testList))
print(testList)


# 1. 일반 함수 버전
def plus_two(x):
    return x + 2


result1 = list(map(plus_two, [1, 2, 3, 4, 5]))
print(result1)

# 2.  람다 함수 버전
result2 = list(map((lambda x: x + 2), [1, 2, 3, 4, 5]))
print(result2)