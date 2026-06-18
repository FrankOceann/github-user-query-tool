import requests


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


username = input("请输入 GitHub 用户名: ")

user = get_github_user(username)

if user is None:
    print("用户不存在或请求失败")
else:
    print("用户名:", user["login"])
    print("昵称:", user["name"])
    print("公开仓库数量:", user["public_repos"])
    print("粉丝数:", user["followers"])
    print("主页:", user["html_url"])