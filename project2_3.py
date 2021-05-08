import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_columns = 30
pd.options.display.float_format = '{:.2f}'.format

df = pd.read_csv('/Users/joanjohn/Desktop/zipcode.csv')
# print(df)
# df.info()
# print(df.Zipcode[1])
# print(df.City[1])
# print(df.describe())

'''visualizing the frequency distribution of columns'''
df.hist(figsize=(16, 8), bins=100)
plt.show()

'''gets statistics of non numeric columns '''
# print(df.describe(include='object'))
