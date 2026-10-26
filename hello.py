import datetime

name = input("你叫什么名字？")
print("你好，" + name + "，这是你的第一行 Python。")
today = datetime.date.today()
print("今天是：",today)
newyear = datetime.date(2027,1,1)
days = (newyear - today).days
print("距离 2027年1月1日还有",days,"天")