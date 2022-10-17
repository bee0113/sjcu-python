num = int(input('입력'))
if num % 2 == 0:
    print('%d 짝수' % num)
else:
    print('%d 짝수' % num)

id = input('id:')
pw = input('pw:')

if id == 'admin' and pw == '1234':
    print('로그인 성공')
else:
    print('로그인 실패')
