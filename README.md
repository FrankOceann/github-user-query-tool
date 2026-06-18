# GitHub 用户信息查询工具

这是一个 Python 命令行小工具，可以根据 GitHub 用户名查询用户信息，并保存为 txt 文件。

## 功能

- 输入 GitHub 用户名
- 调用 GitHub API 查询用户信息
- 判断用户是否存在
- 保存用户信息到 txt 文件
- 支持从 `.env` 读取默认用户名

## 技术栈

- Python
- requests
- python-dotenv
- GitHub API

## 安装依赖

```bash
pip install -r requirements.txt