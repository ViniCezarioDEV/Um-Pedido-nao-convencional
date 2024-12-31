from tkinter import *
import random

def no():
    fim = Tk()
    fim.geometry('300x100')
    fim.title('Te Amo')
    fim.resizable(width=False, height=False)
    fim['bg'] = '#9e0339'
    label = Label(fim, text='Eu também, Te amo ♥', font='Arial 20 bold', fg='white', bg='#9e0339').pack()
    fim.mainloop()

def motionMouse(event):
    btnYes.place(x=random.randint(0,300), y=random.randint(0,300))

root = Tk()
root.geometry('600x400')
root.title('Surpresa')
root.resizable(width=False, height=False)
root['bg'] = '#c9064a'


label = Label(root, text='VOCÊ QUER NAMORAR COMIGO?', font='Arial 20 bold', fg='white', bg='#c9064a').pack()
btnYes = Button(root, text='Não', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='Sim', font='Arial 20 bold', command=no).place(x=350, y=100)

root.mainloop()