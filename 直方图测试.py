# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:26:36 2020

@author: Administrator
"""

# 模块导入
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

fenlei = "被子"
shijian = "2020年1月"
# 数据导入
one_frame = pd.read_excel(r"C:\Users\Administrator\Desktop\test\mingxi111.xlsx")
one_frame2 = one_frame[one_frame["大类"]==fenlei]
one_frame3 = one_frame2["结算额"].astype(np.int64)

two_frame = pd.read_excel(r"C:\Users\Administrator\Desktop\test\mingxi222.xlsx")
two_frame2 = two_frame[two_frame["大类"]==fenlei]
two_frame3 = two_frame2["结算额"].astype(np.int64)

three_frame = pd.read_excel(r"C:\Users\Administrator\Desktop\test\mingxi333.xlsx")
three_frame2 = three_frame[three_frame["大类"]==fenlei]
three_frame3 = three_frame2["结算额"].astype(np.int64)


my_font=font_manager.FontProperties(fname=r"simhei.ttf")
plt.figure(figsize=(20,5),dpi=80)


plt.subplot(1,3,1)
plt.hist(one_frame3,[x for x in range(3000)][::200],label="一公司")
plt.grid()
plt.xticks(list(range(3000))[::200],rotation=45)
plt.yticks(list(range(600))[::100])
plt.xlabel("价格",fontproperties=my_font)
plt.ylabel("数量",fontproperties=my_font)
plt.title("一公司{}销售数量价格分布 {}".format(fenlei,shijian),fontproperties=my_font)
plt.legend(prop=my_font)

plt.subplot(1,3,2)
plt.hist(two_frame3,[x for x in range(3000)][::200],label="二公司")
plt.grid()
plt.xticks(list(range(3000))[::200],rotation=45)
plt.yticks(list(range(600))[::100])
plt.xlabel("价格",fontproperties=my_font)
plt.ylabel("数量",fontproperties=my_font)
plt.title("二公司{}销售数量价格分布 {}".format(fenlei,shijian),fontproperties=my_font)
plt.legend(prop=my_font)

plt.subplot(1,3,3)
plt.hist(three_frame3,[x for x in range(3000)][::200],label="三公司")
plt.grid()
plt.xticks(list(range(3000))[::200],rotation=45)
plt.yticks(list(range(600))[::100])
plt.xlabel("价格",fontproperties=my_font)
plt.ylabel("数量",fontproperties=my_font)
plt.title("三公司{}销售数量价格分布 {}".format(fenlei,shijian),fontproperties=my_font)
plt.legend(prop=my_font)

plt.savefig(r"价格分布.png")