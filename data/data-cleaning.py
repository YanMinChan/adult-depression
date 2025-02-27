import pandas as pd

# Load dataset
df = pd.read_csv("./data/adult-depression-data.csv")

# Transform dataset
col_order = df['Strata Name'].unique() # save the original order
df_cleaned = df.pivot_table(index="Year", values="Frequency", columns="Strata Name", aggfunc='sum').reindex(columns=col_order)

# Print result and write to csv
with pd.option_context('display.max_rows', 1000, 'display.max_columns', 1000):
    print(df_cleaned)
df_cleaned.to_csv("./data/adult-depression-data-cleaned.csv")

# Summarise dataset
print(f'Describe dataset: \n{df_cleaned.describe()}')
