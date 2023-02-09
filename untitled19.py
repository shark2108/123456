import tkinter
import webbrowser

window = tkinter.Tk()
window.resizable(False, False)
window.geometry('500x620')
window['bg'] = 'gray'

def search():
    webbrowser.open('https://github.com/' + qwe.get() + qwe1.get())

qwe2 = tkinter.Label(text='Username / email: ')
qwe2['bg'] = 'gray'
qwe2['font'] = 'Roboto 12'
qwe2.place(x=50, y=240)
qwe2.focus()

qr = tkinter.PhotoImage(file='.\Suleyman Uteniyazov\123456.py\github.png')
label_photo = tkinter.Label(image=qr)
label_photo.place(x=40, y=45, width=350, height=180)

qwer1 = tkinter.Label(text='Login')
qwer1['font'] = 'Roboto 15'
qwer1['bg'] = 'gray'
qwer1.place(x=0, y=0)

qwer = tkinter.Label(text='Password: ')
qwer['bg'] = 'gray'
qwer['font'] = 'Roboto 12'
qwer.place(x=50, y=320)


qwe = tkinter.Entry(width=40)
qwe.place(x=70, y=270)

qwe1 = tkinter.Entry(width=40)
qwe1.place(x=70, y=350)

qwe2 = tkinter.Button(text='   Login   ', command=search)
qwe2['fg'] = 'white'
qwe2['bg'] = 'green'
qwe2['font'] = 'Roboto 12'
qwe2.place(x=150, y=390)

window.mainloop()
