print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
import tkinter as tk
root = tk.Tk()
root.title("Choosing Languages")
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
    print(f"Bạn đã chọn giá trị: {v.get()}")
    chosen_language = [name for name, val in Languages if val == v.get()][0]
    print(f"Ngôn ngữ được chọn: {chosen_language}")
tk.Label(
    root, 
    text="Choose your favourite\nprogramming language:",
    justify = tk.LEFT,
    padx = 20
).pack(anchor=tk.W) 
for text, val in Languages:
    tk.Radiobutton(
        root, 
        text=text,
        padx = 20, 
        variable=v,          
        command=ShowChoice,  
        value=val            
    ).pack(anchor=tk.W)       
for widget in root.winfo_children():
    widget.destroy()
v.set(1)
tk.Label(
    root, 
    text="Choose your favourite\nprogramming language:",
    justify = tk.LEFT,
    padx = 20
).pack(anchor=tk.W)
for i, (text, val) in enumerate(Languages):
    tk.Radiobutton(
        root, 
        text=text,
        indicatoron = 0,    
        width = 20,         
        padx = 20, 
        pady = 5,           
        variable=v,
        command=ShowChoice,
        value=val
    ).pack(anchor=tk.W)
root.mainloop()
