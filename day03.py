students = ["小明", "小红", "小刚","小李","小吴"]
scores = [88, 95, 59, 98,64]

average =sum(scores)/len(scores)
for i in range(len(students)):
    name = students[i]
    score = scores[i]

    if score >= 60:
        print(name, score, "及格")
    else:
        print(name, score, "不及格")

print("平均分：",average)