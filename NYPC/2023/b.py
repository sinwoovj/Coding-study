data = [
    {"id": 1, "이름": "홍길동", "생년월일": "2000-01-01"},
    {"id": 2, "이름": "김철수", "생년월일": "1995-05-15"},
    {"id": 3, "이름": "이영희", "생년월일": "1988-12-30"},
    # 나머지 데이터도 동일한 형식으로 추가
]

id_name_birthday_dict = {}

for entry in data:
    id_name_birthday_dict[entry["id"]] = {
        "이름": entry["이름"],
        "생년월일": entry["생년월일"]
    }

print(id_name_birthday_dict)
