print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
def read_first_n_lines(file_path, n):
    """Đọc và in ra n dòng đầu tiên của tệp."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i in range(n):
                line = f.readline()
                if not line:
                    break
                print(line, end='') 
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

file_duong_dan = 'D:/a.txt'
so_dong = 3
read_first_n_lines(file_duong_dan, so_dong)
