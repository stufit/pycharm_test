import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
sns.set(font_scale=2.5)
import missingno as msno

import warnings
warnings.filterwarnings('ignore')


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df_train = pd.read_csv('/Users/gaegul/PycharmProjects/pythonProject/케글 타이타닉/2019-1st-ml-month-with-kakr/train.csv')
df_test = pd.read_csv('/Users/gaegul/PycharmProjects/pythonProject/케글 타이타닉/2019-1st-ml-month-with-kakr/test.csv')

# print(df_train.head())
# print('----------------------------------------------')
# print(df_train.describe())
# print('----------------------------------------------')
# print(df_test.describe())
# print('----------------------------------------------')

# f, ax = plt.subplots(1, 2, figsize=(18, 8))
#
# df_train['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
# ax[0].set_title('Pie plot - Survived')
# ax[0].set_ylabel('')
# sns.countplot('Survived', data=df_train, ax=ax[1])
# ax[1].set_title('Count plot - Survived')
#
# plt.show()
#print(df_train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).count())