import datetime

# ===== 今天的课表，必须按时间从早到晚写 =====
courses = [
    ("软件工程专业导论", "寒武 204", 8, 0),
    ("高等数学", "2教 418", 10, 0),
    ("思想道德与法治", "2教 507", 14, 0),
    ("C语音程序设计理论课", "图书馆 610-2", 16, 0),
    ("C语音程序设计实验课","图书馆 610-2", 19, 0)
]
# ==========================================

now = datetime.datetime.now()
print("现在：", now.hour, "点", now.minute, "分")

found = False
for course in courses:
    name = course[0]
    place = course[1]
    hour = course[2]
    minute = course[3]

    class_time = datetime.datetime(now.year, now.month, now.day, hour, minute)
    total_minutes = int((class_time - now).total_seconds() // 60)

    if total_minutes > 0:
        print("下一节课：", name)
        print("地点：", place)
        print("还有", total_minutes // 60, "小时", total_minutes % 60, "分钟")
        found = True
        break

if not found:
    print("今天的课都上完了")
input("按回车键退出...")