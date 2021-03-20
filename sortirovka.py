from datetime import datetime
import os
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title('Сортировка файлов по дате')
window.geometry('500x300+1000+300')

def open_path():
    file_path = filedialog.askdirectory()
    def sortirovka():
        for folder, sublofder, files in os.walk(file_path):
            for file in files:
                path = os.path.join(folder,file)
                d = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d')
                dd = os.path.join(file_path,d)
                if not os.path.exists(dd):
                    os.mkdir(dd)
                os.rename(path,os.path.join(dd,file))
    sortirovka()
    Label(window,text='Успешно',font=40,pady=20).place(x=250,y=200,anchor=CENTER)

lbl = Label(window,text='Выберите путь или вставьте его в поле',font=40,pady=20)
lbl.place(x=250,y=100,anchor=CENTER)

btn = Button(window,text='Выбрать путь',command=open_path)
btn.place(x=250,y=150,anchor=CENTER)

window.mainloop()