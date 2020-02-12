# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:44:51 2020

@author: Administrator
"""
#！usr/bin/env python3
# 导入模块
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# 数据导入
X = np.array([[181,80,44],[177,70,43],[160,60,38],[154,54,37],
     [166,65,40],[190,90,47],[175,64,39],[177,70,40],
     [159,55,37],[171,75,42],[181,85,43]])
display(X)
y = ['male','male','female','female','male',
     'male','female','female','female','male','male']

my_knn = KNeighborsClassifier().fit(X,y)


new_per =np.array([[147,45,35],[175,65,39],[160,46,36]])

result = my_knn.predict(new_per)
print(result)
