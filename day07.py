text = "今天开始学习 AI Agent 开发"

file = open("note.txt", "w", encoding="utf-8")
file.write(text)
file.close()

print("写入完成")