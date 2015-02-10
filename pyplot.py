
# coding: utf-8

# In[7]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ts = pd.Series(randn(1000), index=pd.date_range('1/1/2000',periods=1000))
ts = ts.cumsum()
ts.plot()

