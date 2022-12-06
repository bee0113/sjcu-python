f = open('list.txt', 'w')
while True:
    name = input('name : ')
    if not name:
        break
    age = input('age:')
    f.write(name + age + '\n')
print('저장')
f.close()
