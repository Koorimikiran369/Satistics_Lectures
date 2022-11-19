#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

def central_limit_theorem(data,col,N,n):
    pop_mean = data[col].mean()
    print('mean of {} is {}'.format(col,pop_mean))
    sample_means = []
    for i in range(N):
        sample_means.append(data[col].sample(n).mean())
    print('mean of sample means is {}'.format(np.array(sample_means).mean()))
    sns.histplot(sample_means,kde = True)
    plt.show()

