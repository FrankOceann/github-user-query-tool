import json

json_text ='{"name" : "小明","age" : 18, "score" : 88}'

student = json.loads(json_text)

print(student)
print(type(student))
print(student["name"])
print(student["score"])