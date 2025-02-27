import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sb

# Load data
df = pd.read_csv('./data/adult-depression-data-cleaned.csv')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)

# Line plot, scatter plot

