# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:00:25 2020

@author: Administrator
"""

# 模块导入
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 日期设置
def get_date_list(begin_date,end_date):
    date_list = [x.strftime('%Y-%m-%d') for x in list(pd.date_range(start=begin_date, end=end_date))]
    return date_list
dates=get_date_list("2019-12-27","2020-1-15")

# 字体设置
my_font = font_manager.FontProperties(fname=r"simhei.ttf")

# 分类设置
shijian = "2020年1月"
fenlei_list = ["天然乳胶枕","进口乳胶枕","红豆绒2.0","红豆绒合计"]
list_rujiao = ["HB9ZD01140", "HA0ZD03970"]
list_rujiaojk = ["HB9ZD01120","HB9ZD01130"]
list_hongdour2 = ["HB9SD02011","HB9SD02012","HB9SD02221","HB9SD02222","HB9SD06950"]
list_hongdourh = ["HB9SD01851","HB9SD01852","HB9SD01981","HB9SD01982","HB9SD01983",
                  "HB9SD01985","HB9SD01991","HB9SD01992","HB9SD02011","HB9SD02012",
                  "HB9SD02051","HB9SD02052","HB9SD02061","HB9SD02062","HB9SD02081",
                  "HB9SD02082","HB9SD02131","HB9SD02132","HB9SD02211","HB9SD02221",
                  "HB9SD02222","HB9SD02341","HB9SD02361","HB9SD02362","HB9SD02661",
                  "HB9SD02662","HB9SD02671","HB9SD02672","HB9SD05181","HB9SD05182",
                  "HB9SD05190","HB9SD06011","HB9SD06012","HB9SD06021","HB9SD06022",
                  "HB9SD06950","HB9SD07181"]
param = list_hongdourh
fenlei = fenlei_list[3]

# 数据导入
one_frame = pd.read_excel(r"C:\Users\Administrator\Desktop\test\mingxi111.xlsx")
two_frame = pd.read_excel(r"C:\Users\Administrator\Desktop\test\mingxi222.xlsx")
three_frame = pd.read_excel(r"C:\Users\Administrator\Desktop\test\mingxi333.xlsx")

one_frame2 = one_frame.loc[one_frame["商品代码"].isin(param)]
one_frame3 = pd.DataFrame(one_frame2,columns=["单据日期","数量"])
mydata1 = one_frame3.groupby(by="单据日期").sum()
finaldata1 = pd.DataFrame(mydata1,index=dates).fillna(0)
        
two_frame2 = two_frame.loc[two_frame["商品代码"].isin(param)] 
two_frame3 = pd.DataFrame(two_frame2,columns=["单据日期","数量"])
mydata2 = two_frame3.groupby(by="单据日期").sum()
finaldata2 = pd.DataFrame(mydata2,index=dates).fillna(0)
        
three_frame2 = three_frame.loc[three_frame["商品代码"].isin(param)]
three_frame3 = pd.DataFrame(three_frame2,columns=["单据日期","数量"])
mydata3 = three_frame3.groupby(by="单据日期").sum()
finaldata3 = pd.DataFrame(mydata3,index=dates).fillna(0)
    
    
plt.figure(figsize=(10,7),dpi=80)
plt.plot(finaldata1.cumsum(),"r:.",label = "一公司")
plt.plot(finaldata2.cumsum(),"y-.",label = "二公司")
plt.plot(finaldata3.cumsum(),"b--",label = "三公司")
    
plt.grid()
plt.xticks(dates[::2],rotation=45,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("日期",fontproperties=my_font)
plt.ylabel("累计销量",fontproperties=my_font)
plt.title("{}销售趋势图  {}".format(fenlei,shijian),fontproperties=my_font)
plt.legend(prop=my_font,loc="upper left")
    
plt.savefig("销售趋势.png")
plt.show()