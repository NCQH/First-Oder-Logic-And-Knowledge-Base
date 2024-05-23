def read_sentences_from_file(file_path):
    """
    Đọc các câu từ một file văn bản và trả về danh sách các câu.

    Args:
        file_path (str): Đường dẫn đến file văn bản.

    Returns:
        List[str]: Danh sách các câu trong file.
    """
    sentences = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Đọc toàn bộ nội dung của file
            content = file.readlines()
            # Loại bỏ các dòng trống và khoảng trắng thừa
            sentences = [line.strip() for line in content if line.strip()]
    except FileNotFoundError:
        print(f"File {file_path} không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    return sentences