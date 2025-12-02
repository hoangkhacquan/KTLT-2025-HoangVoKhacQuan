print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
from tkinter import *
import tkinter.messagebox as messagebox
def OpenFile():
    messagebox.showinfo("Menu Action", "Bạn đã chọn: Open File")
def ExitApp():
    if messagebox.askokcancel("Thoát", "Bạn có chắc chắn muốn thoát khỏi ứng dụng?"):
        root.destroy()
def InsText():
    messagebox.showinfo("Menu Action", "Bạn đã chọn: Insert Text")

def InsPic():
    messagebox.showinfo("Menu Action", "Bạn đã chọn: Insert Picture")

def AboutApp():
    messagebox.showinfo("Thông tin", "Đây là một ứng dụng minh họa Menu Bar Tkinter.")
root = Tk()
root.title("tk") 
menu = Menu(root)
root.config(menu=menu) 
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu) 
filemenu.add_command(label="New", command=lambda: messagebox.showinfo("Menu Action", "Bạn đã chọn: New File"))
filemenu.add_command(label="Open", command=OpenFile) 
filemenu.add_separator() 
filemenu.add_command(label="Exit", command=ExitApp) 

insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu) 

insertmenu.add_command(label="Text", command=InsText) 
insertmenu.add_command(label="Picture", command=InsPic) 

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=AboutApp)

root.mainloop()
