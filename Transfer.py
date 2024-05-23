import os
from openai import OpenAI
from dotenv import load_dotenv
from loadData import *
load_dotenv()


# Ví dụ sử dụng hàm
sentences_path = './Data/KnowledgeBase.txt'
queries_path = './Data/Queries.txt'

sentences = read_sentences_from_file(sentences_path)
queries = read_sentences_from_file(queries_path)

# In ra các câu
# for sentence in sentences:
#     print(sentence)

prompt_goc = "Hãy chuyển các câu sau thành dạng quy tắc logic..\n" \
             "Ví dụ:\n"
cau_goc = [
    "UET thuộc VNU",
    "Cái gì thuộc UET thì thuộc VNU",
    "Harry lấy thuốc TeaTree",
    "Nếu có tương tác nhẹ giữa 2 sản phẩm thì in cảnh báo",
    "Nếu có tương tác trung bình giữa 2 sản phẩm thì kêu cảnh báo",
    "Huy không nuôi chó",
    "Cái gì thuộc FEMA thì thuộc UET",
    "Toà G2 thuộc UET",
    "Trường ULIS thuộc VNU"
]
cau_chuyen = [
    "Belong(UET, VNU)",
    "Belong(x, UET) => Belong(x, VNU)",
    "Take(Harry,TeaTree)",
    "MildInteract(x,y) & Take(p,x) & Take(p,y) => PrintAlert(p)",
    "MediumInteract(x,y) & Take(p,x) & Take(p,y) => RingAlert(p)",
    "~Adopt(Huy, Dog)",
    "Belong(x, FEMA) => Belong(x, UET)",
    "Belong(G2, UET)",
    "Belong(ULIS, VNU)"
]
cau_goc_va_cau_chuyen = [
    f"Câu gốc: {goc}, Câu chuyển: {chuyen}\n" for goc, chuyen in zip(cau_goc, cau_chuyen)
]

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("API_KEY"),
)

def UpdateKB():
    prompt = prompt_goc + ''.join(cau_goc_va_cau_chuyen) + "Dữ liệu mới:"
    for sentence in sentences:
        prompt = prompt + "\n" + sentence

    # In prompt hoàn chỉnh để kiểm tra
    # print(prompt)

    # Gửi prompt và yêu cầu câu trả lời từ API
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    # Lấy câu trả lời từ kết quả trả về
    response = chat_completion.choices[0].message.content

    # print("Prompt: ", prompt)
    # print("Câu trả lời từ AI:", response)

    with open("./Data/transferSentences.txt", "w", encoding='utf-8') as file:
        file.write(str(len(sentences))+"\n")
        for line in response:
            file.write(line)
    file.close()

def UpdateQueries():
    prompt = prompt_goc + ''.join(cau_goc_va_cau_chuyen) + "Dữ liệu mới:"
    for query in queries:
        prompt = prompt + "\n" + query

    # In prompt hoàn chỉnh để kiểm tra
    # print(prompt)
    # Gửi prompt và yêu cầu câu trả lời từ API
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    # Lấy câu trả lời từ kết quả trả về
    response = chat_completion.choices[0].message.content

    # print("Prompt: ", prompt)
    # print("Câu trả lời từ AI:", response)

    with open("./Data/transferQueries.txt", "w", encoding='utf-8') as file:
        file.write(str(len(queries))+"\n")
        for line in response:
            file.write(line)
    file.close()