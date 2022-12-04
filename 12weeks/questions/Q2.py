# 웹사이트 패스워드가 'sejong'일 때 인증처리를 하는 프로그램

from tkinter import *
from tkinter import messagebox


def login():
    if pw.get() == 'sejong':
        messagebox.showinfo('success', '로그인성공')
    else:
        messagebox.showinfo('fail', '패스워드오류')

w = Tk()
w.title('Welcome to SEJONG!!')
label1 = Label(w, text='패스워드')
pw = Entry(w, show='*')
btn1 = Button(w, text='확인', command=login)
btn2 = Button(w, text='종료', command=quit)
label1.pack()
pw.pack()
btn1.pack()
btn2.pack()
w.geometry('300x200')
