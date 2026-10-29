import pandas as pd

# ===== 认可哪些写法算「交了」（认不全就往里加）=====
交了词 = ["是", "已交", "交了", "交", "已提交", "提交", "完成",
          "ok", "yes", "y", "1", "true", "√", "✓", "到", "到了"]

# ===== 认可哪些写法算「没交」=====
没交词 = ["否", "没交", "未交", "未提交", "未", "没",
          "no", "n", "0", "false", "×", "✗", "x"]


def 转文字(v):
    """把单元格的值统一成字符串。空单元格给空串，数字 1.0 给 "1"。"""
    if pd.isna(v):
        return ""
    if isinstance(v, float) and v == int(v):
        return str(int(v))
    return str(v).strip()


df = pd.read_excel("data.xlsx")
print("总人数：", len(df))

交了 = []
没交 = []
看不懂 = []

for i in range(len(df)):
    姓名 = 转文字(df.loc[i, "姓名"])
    if 姓名 == "":
        continue

    原值 = 转文字(df.loc[i, "是否提交"])
    值 = 原值.lower().replace(" ", "")

    if 值 in 交了词:
        交了.append(姓名)
    elif 值 in 没交词:
        没交.append(姓名)
    else:
        看不懂.append(姓名 + "（填的是「" + (原值 if 原值 else "空") + "」）")

print("✅ 已交", len(交了), "人：", "、".join(交了))
print("❌ 没交", len(没交), "人：", "、".join(没交))

if 看不懂:
    print("⚠️  填得看不懂", len(看不懂), "人：")
    for x in 看不懂:
        print("   -", x)
    print("这些人需要你去问一下，程序不知道他们算不算交了。")