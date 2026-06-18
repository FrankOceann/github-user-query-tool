from config import GITHUB_USERNAME
from github_tools import get_github_user, save_user_info


def main():
    username = input(f"请输入 GitHub 用户名，直接回车默认查询 {GITHUB_USERNAME}: ")

    if username == "":
        username = GITHUB_USERNAME

    user = get_github_user(username)

    if user is None:
        print("用户不存在或请求失败")
    else:
        print("查询成功")
        save_user_info(user)


if __name__ == "__main__":
    main()