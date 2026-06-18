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

## 项目结构

```text
week01-python-basic
  .gitignore
  config.py
  github_tools.py
  main.py
  requirements.txt
  README.md
```

## 文件说明

- `main.py`：程序入口，负责接收用户输入和控制主流程。
- `github_tools.py`：负责查询 GitHub API 和保存用户信息。
- `config.py`：负责读取 `.env` 配置。
- `requirements.txt`：记录项目依赖。
- `.gitignore`：控制哪些文件不上传到 GitHub。

## 安装依赖

先创建并激活虚拟环境：

```bash
python -m venv .venv
.venv\Scripts\Activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

## 配置环境变量

在项目根目录新建 `.env` 文件：

```text
GITHUB_USERNAME=octocat
```

说明：`.env` 文件不要上传到 GitHub，已经在 `.gitignore` 中忽略。

## 运行项目

确认虚拟环境已经激活后运行：

```bash
python main.py
```

看到提示后，可以输入 GitHub 用户名：

```text
octocat
```

也可以直接回车，使用 `.env` 中配置的默认用户名。

## 示例输出

```text
请输入 GitHub 用户名，直接回车默认查询 octocat:
查询成功
用户信息已保存到: octocat.txt
```
