from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random
import os
import shutil
import subprocess

root = tk.Tk()
root.title("Random_roll_call")
root.geometry("800x500")
root.resizable(False, False)
root.config(bg="#4CE012")
top = Label(root, text="让我看看是谁被点到了", font=("Arial", 40),bg="#4CE012", fg="white")
top.pack()
os.mkdir("plugin") if not os.path.exists("plugin") else None

fullscreen_var = tk.BooleanVar(value=True)

rname = ""

name = Label(root, text= rname, font=("Arial", 100), bg="#4CE012", fg="blue")
name.pack()

names = [] 
rolling = False 

def addName():
    global names
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    with open(file_path, 'r', encoding='utf-8') as file:
        names = [line.strip() for line in file if line.strip()]
    if not names:
        messagebox.showerror(":(", "名单不能为空！")

def roll_name():
    global rname
    if not names:
        name.config(text="名单为空")
        return
    rname = random.choice(names)
    name.config(text=rname)
    if rolling:
        root.after(50, roll_name)

def forcall():
    global rolling
    if not names:
        messagebox.showerror(":(", "先导入名单")
        return
    rolling = True
    roll_name()

def call():
    global rolling
    rolling = False
    if fullscreen_var.get():
        fullscreen = tk.Toplevel(root)
        fullscreen.attributes("-fullscreen", True)
        fullscreen.config(bg="#E0A912")
        label = Label(fullscreen, text="喜  报\n"+rname+"\n中奖了！！！", font=("Arial", 140), bg="#E0A912", fg="blue")
        label.pack(expand=True)
        close = Button(fullscreen, text="关闭", font=("Arial", 40), command=fullscreen.destroy, bg="#3812E0", fg="white")
        close.pack(pady=40)
        fullscreen.after(5000, fullscreen.destroy)

def houtai():
    global window1
    window1 = tk.Toplevel(root)
    window1.title("后台管理")
    window1.geometry("400x300")
    window1.resizable(False, False)
    window1.config(bg="#12C1E0")
    addNameList = Button(window1, text="手动选择名单", font=("Arial", 20), bg="#4CE012", fg="white", command=addName)
    addNameList.pack()
    text1 = Label(window1, text="   ", font=("Arial", 40), bg="#12C1E0", fg="white")
    text1.pack()
    more = Button(window1, text="使用扩展", font=("Arial", 20), bg="#4CE012", fg="white", command = plugin)
    more.pack()
    check = Checkbutton(window1, text="全屏通缉", variable=fullscreen_var, font=("Arial", 16), bg="#12C1E0", fg="white", selectcolor="#12C1E0", activebackground="#12C1E0")
    check.pack(pady=10)
    c = Label(window1,text='❗若选择全屏通缉，以全屏通缉上面的名字为准',bg="#12C1E0", fg="red", font=("Arial", 10))
    c.pack()

def plugin():
    global window2, entry
    window2 = tk.Toplevel(window1)
    window2.title("扩展功能")
    window2.geometry("400x300")
    window2.resizable(False, False)
    window2.config(bg="#CCAF08")
    t = Label(window2, text="输入你已经添加的扩展的文件名", font=("Arial", 20), bg="#CCAF08", fg="white")
    t.pack()
    entry = tk.Entry(window2, font=("Arial", 20), bg="#CCAF08", fg="black")
    entry.pack()
    ButtonAddPlugin = Button(window2, text="添加扩展", font=("Arial", 10), bg="#FFFFFF", fg="black", command=addPlugin)
    ButtonAddPlugin.place(x=50, y=200)
    ButtonUsePlugin = Button(window2, text="使用扩展", font=("Arial", 10), bg="#FFFFFF", fg="black", command=usePlugin)
    ButtonUsePlugin.place(x=200, y=200)

def usePlugin():
    plname = entry.get()
    subprocess.run(["python", f"plugin/{plname}.py"], check=True)

def addPlugin():
    plugin_path = filedialog.askopenfilename(title="选择扩展文件", filetypes=[("Python Files", "*.py")])
    if not plugin_path:
        return
    shutil.copy(plugin_path, "plugin/")
    messagebox.showinfo(":)", "已添加")


houtai1 = Button(root, text="后台管理", font=("Arial", 10), bg="#A2E012", fg="white", command=houtai)
houtai1.place(x=600, y=400)

start = Button(root, text="开始点名", font=("Arial", 20), bg="#A2E012", fg="white", command=forcall)
start.place(x=100, y=400)

stop = Button(root, text="停", font=("Arial", 20), bg="#A2E012", fg="white", command=call)
stop.place(x=500, y=400)

mainloop()