print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
def read_last_n_lines(file_path, n):
    """Đọc và in ra n dòng cuối cùng của tệp."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
        
        last_n_lines = all_lines[-n:]
        
        for line in last_n_lines:
            print(line, end='')
            
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

file_duong_dan = 'D:/a.txt'
so_dong = 3
read_last_n_lines(file_duong_dan, so_dong)
