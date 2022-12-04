# <요구사항>
# 사용자로부터 아이디, 패스워드를 입력 받아 로그인 인증을 처리하는 프로그램을 완성하시오.
# – 아이디,패스워드둘다맞으면로그인성공메시지를출력하고 둘중의하나이상틀리면적절한오류메시지출력
# – 초기아이디:'sejong',비번:'1234'
from tkinter import *
from tkinter.messagebox import *


def login():
    if sid.get() == 'sejong':
        if spw.get() == '1234':
            showinfo('success', '로그인 성공')
        else:
            # messagebox.showinfo('fail', '패스워드 오류')
            showinfo('fail', '패스워드 오류')
    else:
        showinfo('fail', '회원가입')


w = Tk()
w.title('Welcome to SEJONG!!')
logo = Label(w, text='세사대-온라인 강의실', fg='green') # fg => 글자색 변경, bg => 배경색 변경
sid = Entry(w)
spw = Entry(w, show='*')
btn1 = Button(w, text='확인', command=login)
btn2 = Button(w, text='종료', command=quit)

# 위에 만든 위젯 붙이기
logo.pack()
sid.pack()
spw.pack()
btn1.pack()
btn2.pack()

w.geometry('300x200')
