import requests


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def save_user_info(user):
    content = f"""GitHub 用户信息
用户名: {user["login"]}
昵称: {user["name"]}
公开仓库数量: {user["public_repos"]}
粉丝数: {user["followers"]}
主页: {user["html_url"]}
"""

    filename = f'{user["login"]}.txt'

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print("用户信息已保存到:", filename)


username = input("请输入 GitHub 用户名: ")

user = get_github_user(username)

if user is None:
    print("用户不存在或请求失败")
else:
    print("查询成功")
    save_user_info(user)