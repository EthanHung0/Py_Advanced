"""1) book_module.py

Lớp Book có các thuộc tính: title, author, year.
Phương thức __str__() trả về:
"Tên sách - Tác giả (Năm xuất bản)"


2) library_module.py
Tạo lớp Library với nhiều phương thức:

add_book(book)
→ Thêm một sách vào thư viện.

list_books()
→ In ra tất cả sách trong thư viện.
Nếu thư viện rỗng, in: "Thư viện chưa có sách nào.".

find_by_title(keyword)
→ Tìm tất cả sách có tiêu đề chứa keyword (không phân biệt hoa/thường).

find_by_author(author_name)
→ Tìm tất cả sách của một tác giả cụ thể.

remove_book(title)
→ Xoá sách theo tên (nếu có nhiều sách trùng tên thì xoá hết).

count_books()
→ Trả về số lượng sách hiện có trong thư viện.


3) main.py

Nhập số lượng sách từ người dùng.
Với mỗi sách: nhập title, author, year.
Nếu year không phải số → thông báo "Năm xuất bản phải là số!" và bỏ qua sách đó.
Sau khi nhập xong:
In danh sách tất cả sách.
In tổng số sách có trong thư viện.
Cho phép tìm sách theo tiêu đề.
Cho phép tìm sách theo tác giả.
Cho phép xoá sách theo tên và in lại danh sách.


Ví dụ chạy chương trình
Input:

Nhập số sách: 2 Nhập tên sách: Dế Mèn Phiêu Lưu Ký Nhập tác giả: Tô Hoài Nhập năm xuất bản: 1941 
Nhập tên sách: Harry Potter Nhập tác giả: J.K. Rowling Nhập năm xuất bản: abc
Output:


Năm xuất bản phải là số!
Danh sách sách trong thư viện:
- Dế Mèn Phiêu Lưu Ký - Tô Hoài (1941)
Tổng số sách: 1

Tìm theo tiêu đề "Harry":
(Không tìm thấy sách nào)

Tìm theo tác giả "Tô Hoài":
- Dế Mèn Phiêu Lưu Ký - Tô Hoài (1941)

Xoá sách "Dế Mèn Phiêu Lưu Ký"
Danh sách sách trong thư viện:
Thư viện chưa có sách nào.
"""