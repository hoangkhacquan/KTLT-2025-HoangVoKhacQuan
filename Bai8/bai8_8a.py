print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
import tkinter as tk
root = tk.Tk()
root.title("Thông Tin Cá Nhân")

info_frame = tk.LabelFrame(
    root, 
    text="Thông Tin Cá Nhân", 
    padx=10, 
    pady=10
)
info_frame.pack(padx=10, pady=10, fill="x")
data = {
    "Họ Tên": "Hoàng Võ Khắc Quân",
    "Ngày tháng năm sinh": "25/10/2006",
    "MSSV": "245752021610150",
    "Ngành học": "KTDK&TDH"
}
row_num = 0
for label_text, value_text in data.items():
    tk.Label(
        info_frame, 
        text=f"{label_text}:", 
        anchor="w", 
        font=('Arial', 10, 'bold') 
    ).grid(row=row_num, column=0, sticky="w", padx=5, pady=2)
    tk.Label(
        info_frame, 
        text=value_text, 
        anchor="w"
    ).grid(row=row_num, column=1, sticky="w", padx=5, pady=2)
    
    row_num += 1
