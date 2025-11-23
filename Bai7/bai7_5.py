print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
def append_and_display_file(file_path, text_to_append):
    """Nối văn bản vào cuối tệp, sau đó đọc và in toàn bộ nội dung."""
    
    try:
        with open(file_path, 'a', encoding='utf-8') as myfile:
            myfile.write(text_to_append + '\n')
    except Exception as e:
        print(f"Lỗi khi ghi file: {e}")
        return 

    try:
        with open(file_path, 'r', encoding='utf-8') as myfile:
            content = myfile.read()
            print("\n--- Nội dung tệp sau khi nối ---")
            print(content)
            print("---------------------------------")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")


file_duong_dan = 'abc.txt'
noi_dung_them = "Đây là dòng được thêm vào sau."

print("Lần chạy 1: Khởi tạo tệp.")
append_and_display_file(file_duong_dan, "Python la ngon ngu lap trinh.")

print("\nLần chạy 2: Nối thêm văn bản.")
append_and_display_file(file_duong_dan, noi_dung_them)
