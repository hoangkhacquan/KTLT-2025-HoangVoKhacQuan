print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
from tkinter import *
window = Tk() 
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
def clicked():
    """Thay đổi nội dung của Label khi nút được nhấn."""
    lbl.configure(text="Button was clicked !!") 
btn = Button(
    window, 
    text="Click Me", 
    command=clicked,        
    bg="green",              
    fg="white"              
)
btn.grid(column=1, row=0)

window.mainloop()
