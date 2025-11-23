print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
def count_lines(file_path):
    """Đếm và in ra tổng số dòng trong tệp."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            line_count = len(f.readlines())
            print(f"Tổng số dòng trong tệp là: {line_count}")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

count_lines('D:/a.txt')
