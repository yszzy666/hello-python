import pandas as pd

df = pd.read_excel("data.xlsx")

print("总人数：", len(df))

没交 = df[df["是否提交"] == "否"]

if len(没交) == 0:
    print("全部交齐了 ✅")
else:
    print("没交的：")
    for 姓名 in 没交["姓名"]:
        print(" -", 姓名)
    print("还差", len(没交), "个人")