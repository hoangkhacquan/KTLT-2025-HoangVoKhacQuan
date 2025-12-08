print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
import tkinter as tk
from tkinter import messagebox
def show_radio_choice():
    """Hiển thị lựa chọn Radio Button đang được chọn (1, 2, hoặc 3)."""
    selected_value = radio_var.get()
    messagebox.showinfo("Lựa Chọn", f"Thông tin nút radio button đang lựa chọn: Số {selected_value}")
root = tk.Tk()
root.title("Welcome") 
radio_frame = tk.LabelFrame(
    root, 
    text="", 
    padx=10, 
    pady=10
)
radio_frame.pack(padx=10, pady=10, fill="x")
radio_var = tk.IntVar()
radio_var.set(1) 
choices = [("First", 1), ("Second", 2), ("Third", 3)]

col_num = 0
for text, value in choices:
    tk.Radiobutton(
        radio_frame,
        text=text,
        variable=radio_var, 
        value=value,        
    ).grid(row=0, column=col_num, padx=5, sticky="w")
    col_num += 1
click_button = tk.Button(
    radio_frame,
    text="Click Me",
    command=show_radio_choice, 
    bg="#4CAF50", 
    fg="white", 
    padx=10
)
click_button.grid(row=0, column=col_num, padx=(15, 0))
root.mainloop()
