try:
    with open("note2.txt", "r", encoding="utf-8") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("文件不存在，请检查文件名")