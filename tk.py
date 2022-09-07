import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sq


con = sq.connect("tk.db")
cur = con.cursor()
#cur.execute("CREATE TABLE tkdb(label1, label2)")
def add_text(entry1, entry2):
    cur.execute("insert into tkdb (label1, label2) values ('entry1', 'entry2')")
    con.commit()


window = tk.Tk()
window.title("My app")
window.minsize(width = 300, height = 300)
window.maxsize(width = 500, height = 500)

def text_():
    text.insert(tk.END, entry1.get())
    text.insert(tk.END, entry2.get())
    if len('tk.db') > 0:   #Не знаю яку умову вписати, щоб перевірити чи заповнена база даних
        messagebox.showinfo("Result", "Anyway, it's ok!")

label1 = tk.Label(text = "Hello world", bg = "black", fg = "white")
label1.pack()

label2 = tk.Label(text = "I'm fine", bg = "yellow", fg = "blue")
label2.pack()

button = tk.Button(text = "Push me", bg = "white", fg = "red", command=text_)
button.pack()

entry1 = tk.Entry()
entry1.pack()

entry2 = tk.Entry()
entry2.pack()

text = tk.Text(width = 40, height = 40, wrap="word")
scrollbar = Scrollbar(orient=VERTICAL, command=text.yview)
scrollbar.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollbar.set)
text.pack()


window.mainloop()