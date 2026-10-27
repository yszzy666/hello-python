import datetime

# ===== 今天的课表，必须按时间从早到晚写 =====
courses = [
    ("高等数学", "教三 302", 1, 0),
    ("大学英语", "外语楼 105", 2, 0),
    ("程序设计", "计算机楼 401", 3, 0),
    ("体育", "体育馆", 4, 0),
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