import tkinter as tk
import pickle
'''
계산기 프로그램
gui 사용 tkinter
pickle을 통해 save load
'''
ldata=0
rootwindow = tk.Tk()
rootwindow.title("20181452_cal")
rootwindow.geometry("350x500")

frame1 = tk.Frame(rootwindow, width=400, height=70)
frame1.pack(pady=40)

frame2 = tk.Frame(rootwindow, width=400, height=100)
frame2.pack(padx=10, pady=10)

entry = tk.Entry(frame1, width=20, font=("Courier",18), borderwidth=5)
entry.pack()
entry.insert(0,"")

#pickle을 사용 저장, 불러오기 구현
def button_save():
    with open('F:\1sys\pyex\work\cal.pkl', 'wb') as f:
        pickle.dump(entry, f)
def button_load():
    with open(file='cal.pickle', mode='rb') as f:
        ldata=pickle.load(f)
        entry

#버튼 구현
def button_clicked(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_sub():
    first_number = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_mul():
    first_number = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_div():
    first_number = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)

    if math == 'addition':
        entry.insert(0,f_num + int(second_number))

    if math == 'subtraction':
        entry.insert(0,f_num - int(second_number))

    if math == 'multiplication':
        entry.insert(0,f_num * int(second_number))

    if math == 'division':
        entry.insert(0,f_num / int(second_number))


btn7 = tk.Button(frame2,text='7', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(7))
btn7.grid(column=0, row=0, padx=5, pady=5)
btn8 = tk.Button(frame2,text='8', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(8))
btn8.grid(column=1, row=0, padx=5, pady=5)
btn9 = tk.Button(frame2,text='9', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(9))
btn9.grid(column=2, row=0, padx=5, pady=5)

btn4 = tk.Button(frame2,text='4', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(4))
btn4.grid(column=0, row=1, padx=5, pady=5)
btn5 = tk.Button(frame2,text='5', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(5))
btn5.grid(column=1, row=1, padx=5, pady=5)
btn6 = tk.Button(frame2,text='6', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(6))
btn6.grid(column=2, row=1, padx=5, pady=5)

btn1 = tk.Button(frame2,text='1', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(1))
btn1.grid(column=0, row=2, padx=5, pady=5)
btn2 = tk.Button(frame2,text='2', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(2))
btn2.grid(column=1, row=2, padx=5, pady=5)
btn3 = tk.Button(frame2,text='3', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(3))
btn3.grid(column=2, row=2, padx=5, pady=5)

#음수 표현
btn_pm = tk.Button(frame2,text='+/-', padx=5, pady=10, font=("Courier",15),command=lambda: button_clicked('-'))
btn_pm.grid(column=0, row=3, padx=5, pady=5)
btn0 = tk.Button(frame2,text='0', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(0))
btn0.grid(column=1, row=3, padx=5, pady=5)
btn_p = tk.Button(frame2,text='.', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked('.'))
btn_p.grid(column=2, row=3, padx=5, pady=5)

btn_mul = tk.Button(frame2,text='X', padx=15, pady=10, font=("Courier",15),command=button_mul)
btn_mul.grid(column=3, row=0, padx=5, pady=5)
btn_sub = tk.Button(frame2,text='-', padx=15, pady=10, font=("Courier",15),command=button_sub)
btn_sub.grid(column=3, row=1, padx=5, pady=5)
btn_add = tk.Button(frame2, text='+', padx=15, pady=10, font=("Courier",15),command=button_add)
btn_add.grid(column=3, row=2, padx=5, pady=5)
btn_div = tk.Button(frame2, text='/', padx=15, pady=10, font=("Courier",15),command=button_div)
btn_div.grid(column=3, row=3, padx=5, pady=5)
#저장버튼
btn_save = tk.Button(frame2, text='save', padx=5, pady=10, font=("Courier",15),command=button_save)
btn_save.grid(column=0, row=4, padx=1, pady=5)
#로드버튼
btn_load = tk.Button(frame2, text='load', padx=5, pady=10, font=("Courier",15),command=button_load)
btn_load.grid(column=1, row=4, padx=1, pady=5)

btn_c = tk.Button(frame2, text='C', padx=15, pady=10, font=("Courier",15),command=button_clear)
btn_c.grid(column=2, row=4, padx=5, pady=5)

btn_res = tk.Button(frame2, text='=', padx=15, pady=10, font=("Courier",15),command=button_equal)
btn_res.grid(column=3, row=4, padx=5, pady=5)

btn3 = tk.Button(rootwindow,text='9')

rootwindow.mainloop()