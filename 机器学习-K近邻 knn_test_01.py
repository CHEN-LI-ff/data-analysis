# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:05:59 2020

@author: Administrator
"""

#! usr/bin/env python3

# 导入模块
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt


#导入文件
xunlianji = pd.read_excel(r"F:\GIT\机器学习\KNN\训练样本1.xlsx")
train = xunlianji[["动作镜头","接吻镜头"]]
ylabel = xunlianji["电影类别"]
print(xunlianji)
print(train)
print(ylabel)

my_knnmd = KNeighborsClassifier()
my_knnmd.fit(train,ylabel)

newfilm = np.array([[15,2],[4,24],[10,17]])

print(newfilm)

result = my_knnmd.predict(newfilm)
print(result)


plt.scatter(train["动作镜头"],train["接吻镜头"])
plt.scatter(newfilm[:,0],newfilm[:,1],color="red")