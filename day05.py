students = [
    {
        "name": "小明",
        "age": 18,
        "score": 88
    },
    {
        "name": "小红",
        "age": 17,
        "score": 95
    },
    {
        "name": "小刚",
        "age": 18,
        "score": 59
    }
]
for student in students:
    name=student["name"]
    age=student["age"]
    score=student["score"]

    if student["score"] >= 60:
        result="及格"
    else:
        result="不及格"

    print(name,age,score,result)