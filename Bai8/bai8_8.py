print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
import tkinter as tk
from tkinter import messagebox
def show_radio_choice():
    """Hiển thị lựa chọn Radio Button đang được chọn."""
    choice_map = {
        1: "First",
        2: "Second",
        3: "Third"
    }
    selected_value = radio_var.get()
    selected_text = choice_map.get(selected_value, "Không có lựa chọn nào")   
    messagebox.showinfo("Lựa Chọn", f"Thông tin nút radio button đang lựa chọn: {selected_value} ({selected_text})")
root = tk.Tk()
root.title("Thông Tin Cá Nhân & Lựa Chọn")
info_frame = tk.LabelFrame(root, text="Thông Tin Cá Nhân", padx=10, pady=10)
info_frame.pack(padx=10, pady=10, fill="x")
data = {
    "Họ Tên": "Hoàng Võ Khắc Quân",
    "Ngày tháng năm sinh": "25/10/2006",
    "MSSV": "245752021610150",
    "Ngành học": "KTDK&TDH"
}
row_num = 0
for label_text, value_text in data.items():
    tk.Label(info_frame, text=f"{label_text}:", anchor="w", width=20, font=('Arial', 10, 'bold')).grid(row=row_num, column=0, sticky="w", padx=5, pady=2)
    tk.Label(info_frame, text=value_text, anchor="w", width=30).grid(row=row_num, column=1, sticky="w", padx=5, pady=2)   
    row_num += 1
radio_frame = tk.LabelFrame(root, text="Lựa Chọn", padx=10, pady=10)
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
