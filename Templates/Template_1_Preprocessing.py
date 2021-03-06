# https://mp.weixin.qq.com/s/Z98tyZ8VqxiwgjB6BarpUw?scene=25#wechat_redirect
#  Preprocess
# 通用的预处理框架
import pandas as pd
import numpy as np
import scipy as sp

# 文件读取
def read_csv_file(f, logging=False):
    print("==========读取数据=========")
    data =  pd.read_csv(f)
    if logging:
        print(data.head(5))
        print(f, "包含以下列")
        print(data.columns.values)
        print(data.describe())
        print(data.info())
    return data
