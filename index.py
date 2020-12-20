from tkinter import * 
from fizzBuzz import *
window = Tk()

window.title("FizzBuzz")

window.geometry('700x500')
window.resizable(0, 1)
bottom_section = Frame(window, bd=5, relief=RIDGE)
bottom_section.grid(row=1, sticky="WENS")
bottom_section.grid_columnconfigure(0, weight=0)
bottom_section.grid_columnconfigure(1, weight=3)
bottom_section.grid_rowconfigure(0, weight=1)
toolbar_cont = Frame(bottom_section)
toolbar_cont.grid(row=0, column=0, sticky="WENS")
bottom_section.pack()

# Text output
text_output_cont = Frame(bottom_section)
text_output_cont.grid_columnconfigure(0, weight=1)
text_output_cont.grid_columnconfigure(1, weight=0)
text_output_cont.grid_rowconfigure(0, weight=0)
text_output_cont.grid_rowconfigure(1, weight=1)
text_output_cont.grid(row=0, column=1, sticky="WENS")


Label(text_output_cont, text="Output:").grid(row=0, sticky="W")
scrollbar = Scrollbar(text_output_cont)
text_cont = Text(text_output_cont, width=250, height=250)
text_cont.config(state=DISABLED)

text_cont.grid(row=1, column=0,  sticky="WENS")
scrollbar.grid(row=1, column=1, sticky="NS")

text_cont.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_cont.yview)

Label(toolbar_cont, text="Range").grid(column=0, row=0, sticky="W")


def validate_num(cad):
    return cad.isdecimal() or cad == '-' 


def validate_num2(cad):
    return cad.isdecimal()


txt1 = Entry(toolbar_cont, validate='all', validatecommand=(window.register(validate_num), '%S'),width=10)
txt1.focus()
txt1.grid(column=1, row=0)

txt2 = Entry(toolbar_cont,validate='all', validatecommand=(window.register(validate_num2), '%S'), width=10)
txt2.grid(column=1, row=1)


def clicked():
    text_cont.config(state=NORMAL)
    text_cont.insert(END, (main(int(txt1.get()), int(txt2.get())) + '\n')*(int(txt1.get()) < int(txt2.get())) or
                     "the first value should be more than the second value\n")
    text_cont.config(state=DISABLED)


def on_reset_click():
    text_cont.config(state=NORMAL)
    text_cont.delete(1.0, END)
    text_cont.config(state=DISABLED)


btn = Button(toolbar_cont, text="Run", command=clicked)
btn.grid(column=2, row=0, sticky="WE")

btn1 = Button(toolbar_cont, text="clear", command=on_reset_click)
btn1.grid(column=2, row=1, sticky="WE")


window.mainloop()
