name = "吴润南"
age = 22
scores = [88, 76, 92, 60, 45,98]

total = sum(scores)
average = total / len(scores)
high = max(scores)
low = min(scores)

print("姓名:", name)
print("年龄:", age)
print("总分:", total)
print("平均分:", average)
print("最高分",high)
print("最低分",low)
for score in scores:
    if score >= 60:
        print(score, "及格")
    else:
        print(score, "不及格")