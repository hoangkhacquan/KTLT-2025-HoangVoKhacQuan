print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Choosing Languages (Indicators)")
root.geometry('300x250') 
v = tk.IntVar()
v.set(1) 
Languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C#", 5)
]
def ShowChoice():
    chosen_language = [name for name, val in Languages if val == v.get()][0]
    messagebox.showinfo("Lựa Chọn", f"Ngôn ngữ được chọn: {chosen_language} (Giá trị {v.get()})")
tk.Label(
    root, 
    text="Choose your favourite\nprogramming language:",
    justify = tk.LEFT,
    padx = 20,
    font=('Arial', 10, 'bold')
).pack(anchor=tk.W, pady=(10, 5)) 
for text, val in Languages:
    tk.Radiobutton(
        root, 
        text=text,
        indicatoron = 0,    
        width = 20,      
        padx = 20,          
        pady = 5,          
        variable=v,        
        command=ShowChoice, 
        value=val,         
        relief=tk.RAISED    
    ).pack(anchor=tk.W)
root.mainloop()
