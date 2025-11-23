print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
def reverse_file_contents(file_path):
    """Đọc file và in nội dung của từng dòng theo thứ tự đảo ngược."""
    try:
        with open(file_path, 'r') as input_file:
            for line in input_file:
                reversed_line = line.rstrip('\n')[::-1]
                print(reversed_line)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

file_duong_dan = 'D:/a.txt' 
reverse_file_contents(file_duong_dan)
