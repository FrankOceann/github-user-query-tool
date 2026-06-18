import requests


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)
    data = response.json()

    return data


username = input("请输入 GitHub 用户名: ")

user = get_github_user(username)

print("用户名:", user["login"])
print("昵称:", user["name"])
print("公开仓库数量:", user["public_repos"])
print("粉丝数:", user["followers"])
print("主页:", user["html_url"])