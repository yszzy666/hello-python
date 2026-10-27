# hello-pyton

Python 入门练习仓库 —— 从零开始学编程的记录。

## 文件说明

- `hello.py` — 第一个 Python 程序：打招呼、显示今天日期、计算距 2027 年还有多少天
- `countdown.py` — 课程倒计时工具：读入一天课表，自动找出下一节课并计算还剩多久

## 快速开始

需要 Python 3.10 以上。

    python countdown.py

输出示例：

    现在： 13 点 45 分
    下一节课： 程序设计
    地点： 计算机楼 401
    还有 0 小时 14 分钟

## 换成自己的课表

打开 `countdown.py`，修改 `courses` 列表（必须按时间从早到晚排序）：

    courses = [
        ("高等数学", "教三 302", 8, 0),
        ("大学英语", "外语楼 105", 10, 0),
    ]

## 打包成 exe

    python -m pip install pyinstaller
    pyinstaller --onefile countdown.py

生成的文件在 `dist/countdown.exe`，可直接发给没有装 Python 的同学。

## 环境

- Windows 11
- Python 3.15.2