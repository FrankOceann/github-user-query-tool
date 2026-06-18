import requests


def get_api_status():
    url = "https://api.github.com"
    response = requests.get(url)

    if response.status_code == 200:
        return "API 请求成功"
    else:
        return "API 请求失败"


result = get_api_status()
print(result)