import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog, Label, Button

def choose():
    global path, names
    path = filedialog.askopenfilename()
    if not path:
        return
    with open(path, 'r', encoding='utf-8') as file:
        names = [line.strip() for line in file if line.strip()]
        messagebox.showinfo(":>","已加载:"+str(path))


def xiugai():
    if not names:
        messagebox.showerror("错误", "名单不能为空！")
        return
    with open(path, 'a', encoding='utf-8') as file:
        name = enter.get()
        if name in names:
            gl = int(enter2.get())
            for i in range(gl):
                file.write(name+"\n")
            messagebox.showinfo(":>", "修改成功")

root = tk.Tk()
root.title("⚡ 概 率 修 改 器 ⚡")
root.geometry("800x500")
root.resizable(False, False)
root.config(bg="#FF0000")
one = Label(root, text="⚡ 概 率 修 改 器 ⚡", font=("Arial", 40), bg="#FF0000", fg="black")
one.pack()

bu1 = Button(root, text='选择你在随机点名中选择的名单文件', font=("Arial", 20), bg="#660C0C", fg="red", command=choose)
bu1.pack()

two = Label(root, text="将", font=("Arial", 20), bg="#FF0000", fg="black").pack()
enter = tk.Entry(root, font=("Arial", 20), bg="#660C0C", fg="white")
enter.pack()
three = Label(root, text="的名字在文末增加的次数\n越多概率越大", font=("Arial", 20), bg="#FF0000", fg="black").pack()
enter2 = tk.Entry(root, font=("Arial", 20), bg="#660C0C", fg="red")
enter2.pack()
bu2 = Button(root, text='修改', font=("Arial", 20), bg="#660C0C", fg="red",command = xiugai).pack()


mainloop()