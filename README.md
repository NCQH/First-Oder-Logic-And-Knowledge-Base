# First-Oder-Logic-And-Knowledge-Base

Repo này được tạo cho môn Trí tuệ nhân tạo INT3401_20 của nhóm 4

This repo is created for INT3401_20 of group 4

## Mục lục
- [First Order Logic](#first-order-logic)
- [Knowledge Base](#knowledge-base)
- [Xây dựng cơ sở tri thức và suy luận](#Xây-dựng-cơ-sở-tri-thức-và-suy-luận)
## First Order Logic
**First Order Logic** (FOL), hay Logic vị từ cấp 1, là một hình thức biểu diễn được sử dụng trong khoa học, cung cấp một khuôn khổ để định nghĩa các tuyên bố logic về các đối tượng và mối quan hệ của chúng.
### Cú pháp và ngữ nghĩa
#### Symbols (Ký hiệu)
1. Constant symbols: Diễn giải chỉ rõ những đối tượng được đề cập đến
2. Predicate symbols: Diễn giải chỉ rõ mối quan hệ cụ thể trong mô hình
3. Function symbols: Ánh xạ các đối tượng đến các đối tượng khác
#### Terms
1. Constants
2. Variables
3. Function
#### Atomic Sentences
'Brother(Richard, John)' nghĩa là John là anh(em) trai của Richard
#### Complex Sentences
'∀x (Cat(x) → Mammal(x))' nghĩa là "All cats are mammals."

## Knowledge Base
### Xây dựng cơ sở kiến thức
Quá trình xây dựng cơ sở kiến thức là việc tổ chức, lưu trữ và quản lý thông tin đã được cấu hình để hỗ trợ việc tìm kiếm, truy vấn và phân tích dữ liệu một cách hiệu quả. Các cơ sở kiến trúc này có thể được áp dụng trong nhiều lĩnh vực khác nhau như khoa học máy tính, trí tuệ nhân tạo, công nghệ thông tin, y tế, tài chính và nhiều lĩnh vực khác.
### Tính chất của một cơ sở kiến thức tốt
1. Một cơ sở kiến thức tốt cung cấp một bức tranh toàn diện và đầy đủ về lĩnh vực hoặc chủ đề mà nó đại diện. Thông tin trong cơ sở kiến thức phải được xác minh và chính xác, tránh những thông tin sai lệch hoặc không đúng sự thật.
2. Mỗi cơ sở kiến thức có hai đối tượng sử dụng tiềm năng: người đọc và các quy trình suy luận.

## Xây dựng cơ sở tri thức và suy luận
Mục tiêu xây dựng cơ sở tri thức bằng các câu tiếng Việt và các câu truy vấn.

Các câu thuộc cơ sở tri thức sẽ được viết từng dòng trong file KnowledgeBase.txt

Sau đó các câu sẽ được chuyển sang dạng logic bằng cách sử dụng model gpt-3.5-turbo thông qua gọi API trong Tranfer.py

Câu trả lời của model - tức các câu được chuyển - được lưu trong tranferSentences.txt, làm input để lưu vào cơ sở tri thức

