# 我的第一个 Python 程序
# 运行方式：VS Code 里按 F5，或在终端执行 python hello.py

name = "芯火厨娘"
print(f"你好，{name}！这是我的第一行代码。")

# 1. 变量与计算：算一份订单
price = 20          # 一份干锅单价（元）
count = 3           # 份数
total = price * count
print(f"{count} 份干锅，单价 {price} 元，合计 {total} 元")

# 2. 条件判断：满 50 减 10
if total >= 50:
    print(f"满足满减，实付 {total - 10} 元")
else:
    print("没到满减门槛")

# 3. 循环：打印一周复盘清单
days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
for d in days:
    print(f"{d}：学 Python 30 分钟")
