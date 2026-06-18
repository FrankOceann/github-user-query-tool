import requests


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
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