import pandas as pd

df = pd.read_excel("data.xlsx")

print("总人数：", len(df))

交了 = []
没交 = []
看不懂 = []

for i in range(len(df)):
    姓名 = df.loc[i, "姓名"]
    值 = str(df.loc[i, "是否提交"]).strip()

    if 值 == "是":
        交了.append(姓名)
    elif 值 == "否":
        没交.append(姓名)
    else:
        看不懂.append(姓名 + "（填的是「" + 值 + "」）")

print()
print("✅ 已交", len(交了), "人：", "、".join(交了))
print("❌ 没交", len(没交), "人：", "、".join(没交))

if 看不懂:
    print()
    print("⚠️  填得看不懂", len(看不懂), "人：")
    for x in 看不懂:
        print("   -", x)
    print()
    print("这些人需要你去问一下，程序不知道他们算不算交了。")