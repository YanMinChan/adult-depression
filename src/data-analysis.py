import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Load data
df = pd.read_csv('./data/adult-depression-data-cleaned.csv')
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#   print(df)
# print(df.dtypes)

## Descriptive statistics analysis
# Higest depression rate (gender) by year
df_gender = df[["Year", "Male", "Female"]]
genders = ["Male", "Female"]
counts = df_gender[df_gender["Year"]==2012][["Male", "Female"]].values[0].tolist()

fig, axs = plt.subplots(1, 1)
axs.bar(genders, counts)

plt.show()


