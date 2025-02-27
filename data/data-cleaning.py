import pandas as pd

# Load dataset
df = pd.read_csv("adult-depression-data.csv")

# Transform dataset
col_order = df['Strata Name'].unique() # save the original order
df_cleaned = df.pivot_table(index="Year", values="Frequency", columns="Strata Name", aggfunc='sum').reindex(columns=col_order)

# Print result
with pd.option_context('display.max_rows', 1000, 'display.max_columns', 1000):
    print(df_cleaned)
