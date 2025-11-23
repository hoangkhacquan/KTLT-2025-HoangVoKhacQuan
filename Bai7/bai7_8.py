print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
def write_list_to_file(file_path, data_list):
    """Ghi nội dung của danh sách vào tệp, mỗi phần tử một dòng."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for item in data_list:
                f.write(item + '\n')
        print(f"Đã ghi {len(data_list)} mục từ danh sách vào tệp: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
             print("\nNội dung đã ghi:")
             print(f.read())
             
    except Exception as e:
        print(f"Đã xảy ra lỗi khi ghi file: {e}")

shopping_list = ["Trứng", "Sữa tươi", "Bánh mì", "Rau xanh"]
write_list_to_file('D:/shopping_list.txt', shopping_list)
