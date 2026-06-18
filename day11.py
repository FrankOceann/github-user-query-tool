import requests

username = "octocat"
url = f"https://api.github.com/users/{username}"

response = requests.get(url)
data = response.json()

print("用户名:", data["login"])
print("昵称:", data["name"])
print("公开仓库数量:", data["public_repos"])
print("粉丝数:", data["followers"])
print("主页:", data["html_url"])