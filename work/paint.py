import tkinter as tk
import pickle

mycolor = "black"

#그리기, 튜플사용
def paint(event):
    x1, y1 = ( event.x-1 ), ( event.y-1 )
    x2, y2 = ( event.x+1 ), ( event.y+1 )
    canvas.create_oval(x1, y1, x2, y2, fill=mycolor, outline=mycolor)

rootwindow = tk.Tk()
canvas = tk.Canvas(rootwindow)
canvas.pack()

def button_save():
    with open('paint.pickle', 'wb') as f:
        pickle.dump(canvas, f)
def button_load():
    with open(file='paint.pickle', mode='rb') as f:
        canvas=pickle.load(f)
#클릭시 도트를 찍음
canvas.bind("<B1-Motion>", paint)
frame1 = tk.Frame(rootwindow, width=400, height=70)
frame1.pack(pady=40)
#저장버튼
btn_save = tk.Button(frame1, text='save', padx=5, pady=10, font=("Courier",15),command=button_save)
btn_save.grid(column=0, row=4, padx=1, pady=5)
#로드버튼
btn_load = tk.Button(frame1, text='load', padx=5, pady=10, font=("Courier",15),command=button_load)
btn_load.grid(column=1, row=4, padx=1, pady=5)
rootwindow.mainloop()