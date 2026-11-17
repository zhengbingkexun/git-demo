"""D1 实验：内存、栈与堆

运行前先在纸上写下每一行 print 你预期的结果，再运行对照。
运行：python mem_demo.py
"""

import copy
import sys

print("=" * 50)
print("实验一：变量名是标签，不是盒子")
print("=" * 50)

a = [1, 2, 3]
b = a                     # b 和 a 指向同一个对象
print("a、b 是同一个对象吗？", id(a) == id(b))

b.append(4)               # 通过 b 改数据
print("改 b 之后，a 变成什么？", a)

c = a.copy()              # 另开一块内存，复制一份
print("c、a 是同一个对象吗？", id(c) == id(a))
c.append(5)
print("改 c 之后，a 是什么？", a)


print()
print("=" * 50)
print("实验二：栈上放调用，堆上放对象")
print("=" * 50)


def make():
    local = {"k": "v"}    # 这个字典创建在堆上
    print("  函数内部的 id：", id(local))
    return local


d = make()
print("  函数外部的 id：", id(d))


print()
print("=" * 50)
print("实验三：栈是有大小的，递归会把它压爆")
print("=" * 50)

print("当前递归上限：", sys.getrecursionlimit())


def boom(n):
    return boom(n + 1)    # 每次调用都往栈上压一帧


try:
    boom(0)
except RecursionError as e:
    print("栈满了：", e)


print()
print("=" * 50)
print("实验四：copy() 只复制一层，deepcopy() 才是彻底隔离")
print("=" * 50)

nested = [[1], [2]]           # 外层列表里套着两个内层列表
shallow = nested.copy()      # 浅拷贝：只复制外层这张"表"
shallow.append([3])          # 往浅拷贝里加东西，原对象不受影响
print("浅拷贝加了新元素后，原对象：", nested)

shallow[0].append(9)         # 但改内层列表，两个对象共享同一个内层
print("浅拷贝改了内层后，原对象：", nested)     # 内层跟着变！

deep = copy.deepcopy(nested) # 深拷贝：里里外外全复制一份
deep[0].append(8)
print("深拷贝改了内层后，原对象：", nested)     # 这次不受影响
