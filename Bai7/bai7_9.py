print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
import shutil

def copy_file_contents(source_path, destination_path):
    """Sao chép nội dung từ tệp nguồn sang tệp đích."""
    try:
        shutil.copyfile(source_path, destination_path)
        print(f"Đã sao chép nội dung thành công từ:")
        print(f"  Nguồn: {source_path}")
        print(f"  Đích: {destination_path}")
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy tệp nguồn hoặc đường dẫn không hợp lệ.")
    except Exception as e:
        print(f"Đã xảy ra lỗi trong quá trình sao chép: {e}")
        
copy_file_contents('D:/a.txt', 'D:/a_copy.txt')
