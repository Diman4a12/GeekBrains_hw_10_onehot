import random
import pandas as pd
import numpy as np


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data['human'] = np.where(data['whoAmI'] == 'human', 1, 0)
data['robot'] = np.where(data['whoAmI'] == 'robot', 1, 0)
print(data.head())