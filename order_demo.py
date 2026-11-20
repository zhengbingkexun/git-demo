"""D4 实验：变量与类型的三个陷阱

运行前先在纸上写下每一段 print 你预期的结果，再运行对照。
运行：python order_demo.py
"""

# ============================================================
# 陷阱一：浮点数——小数在二进制里除不尽，存的是近似值
# 坑在哪：0.1、0.2 这类十进制小数换成二进制是无限循环，
#         计算机只能存一个最近的近似值，累加后误差就露出来。
# 规矩：金额一律用「整数分」存（xxx_cents），全程不碰小数元。
# ============================================================

print("=" * 50)
print("实验一：浮点数相加不等于肉眼看起来的结果")
print("=" * 50)

print("0.1 + 0.2 =", repr(0.1 + 0.2))
print("0.1 + 0.2 == 0.3 吗？", 0.1 + 0.2 == 0.3)
print("两者的差（误差尾数）：", repr(0.1 + 0.2 - 0.3))

# 重复加 10 次 0.1，看误差怎么攒出来
total = 0.0
for _ in range(10):
    total += 0.1
print("加 10 次 0.1 =", repr(total), "（预期是 1.0）")

# 金额正确姿势：用整数分，先算分，最后才换元
price_cents = 2000          # 20.00 元 = 2000 分
count = 3
total_cents = price_cents * count
print("合计（分）：", total_cents, "= 元：", total_cents / 100)


print()
print("=" * 50)
print("实验二：可变默认参数——默认值只创建一次，被所有调用共享")
print("=" * 50)

# 坑在哪：函数定义时，默认参数 [] 就建好了；
#         之后每次调用不传参，用的都是同一块列表。
#         list / dict / set 是可变的，往里加东西，下一次调用还在。


def add_wrong(item, basket=[]):
    basket.append(item)
    return basket


print("第一次加：", add_wrong("干锅"))
print("第二次加：", add_wrong("奶茶"))   # 干锅居然还在篮子里！


# 修法：默认值写 None，函数内部需要时再新建一个空列表
def add_right(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


print("正确写法第一次：", add_right("干锅"))
print("正确写法第二次：", add_right("奶茶"))


print()
print("=" * 50)
print("实验三：作用域——函数里改全局变量，不加 global 改不动")
print("=" * 50)

# 坑在哪：函数内部对一个变量赋值，Python 就把它当局部变量；
#         没在函数里建过就先加一，会报 UnboundLocalError。
#         想改外面的全局变量，要先声明 global。

counter = 0


def bump_wrong():
    counter += 1          # 这里的 counter 被当成局部变量，还没赋值就先读


try:
    bump_wrong()
except UnboundLocalError as e:
    print("不加 global 的报错：", e)


def bump_right():
    global counter         # 声明：我要用外面那个全局 counter
    counter += 1


bump_right()
bump_right()
print("加了两次之后，全局 counter =", counter)
