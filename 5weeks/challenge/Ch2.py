# 아이디와 패스워드를 입력 받아 로그인 인증 결과를 출력한다. 빈칸을 완성하시오.
# - 아이디('admin'), 패스워드('1234') 둘 다 맞으면 로그인 성공
#   메시지를 출력하고 둘 중의 하나 이상 틀리면 오류메시지 출력
id = input('아이디 입력:')
pw = input('패스워드 입력:')
if id == 'admin' and pw == '1234':
    print('로그인 성공')
else:
    print('로그인 실패')