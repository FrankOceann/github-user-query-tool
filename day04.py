def check_pass(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"

def get_level(score):
    if score>=90:
        return"优秀"
    elif score>=80:
        return "良好"
    elif score>=60:
        return "及格"
    else:
        return "不及格"

students = ["小明", "小红", "小刚","小李","小吴"]
scores = [88, 95, 59,89,76]

for i in range(len(students)):
    name = students[i]
    score = scores[i]
    result = get_level(score)

    print(name, score, result)