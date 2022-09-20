import tkinter as tk
import pickle

rootwindow = tk.Tk()

rootwindow.title("20181452_textpad")
rootwindow.geometry("350x500")
rootwindow.resizable(True, True)

# root 안의 frame
frame = tk.Frame(rootwindow)
frame.pack(fill="both", expand=True)
frame1 = tk.Frame(rootwindow, width=400, height=100)
frame1.pack(padx=10, pady=10)
#스크롤바
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# frame 안의 텍스트 입력창과 스크롤바 기능 추가
# (yscrollcommand = scrollbar.set 안하면 스크롤이 계속 제자리로 돌아감.)
txt = tk.Text(frame, yscrollcommand = scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

def button_save():
    with open('txt.pkl', 'wb') as f:
        pickle.dump(txt, f)
def button_load():
    with open(file='txt.pkl', mode='rb') as f:
        txt=pickle.load(f)

#저장버튼
btn_save = tk.Button(frame1, text='save', padx=5, pady=10, font=("Courier",15),command=button_save)
btn_save.grid(column=0, row=0, padx=1, pady=5)
#로드버튼
btn_load = tk.Button(frame1, text='load', padx=5, pady=10, font=("Courier",15),command=button_load)
btn_load.grid(column=1, row=0, padx=1, pady=5)

rootwindow.mainloop()