note = """今天学习 with open 文件读写
明天继续学习异常处理
以后要做AI Agent
你好"""

with open("note2.txt", "w", encoding="utf-8") as file:
    file.write(note)

print("写入完成")

with open("note2.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("读取内容:")
print(content)