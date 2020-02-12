# ！/usr/bin/env python
# -*- coding: utf-8 -*-

# 获得数字母和数字组合的激活码生成器
# 用自己的办法尝试，不管方法是不是很笨
# 应该有更好的方法，等我学会了再来修改代码
import string
import random
fanwei=string.ascii_letters+string.digits
# 定义一个函数，变量为输出几个激活码
def cerate_jihuoma(x):  # x等于几，输出几个激活码
    while x > 0:
        i = 0
        xulie_str = ""
        while i < 15:  # i小于数字几，生成几位数
            xulie_num = random.randint(0, len(fanwei) - 1)
            xulie_str += fanwei[xulie_num]
            i += 1
        print(xulie_str)
        x -= 1

cerate_jihuoma(200)