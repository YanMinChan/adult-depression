import pandas as pd

# Load dataset
df = pd.read_csv("./data/adult-depression-data.csv")

# Transform dataset
col_order = df['Strata Name'].unique() # save the original order
df_cleaned = df.pivot_table(index="Year", values="Frequency", columns="Strata Name", aggfunc='sum').reindex(columns=col_order)

# Replace some symbols that will cause issues
df_cleaned.columns = df_cleaned.columns.str.replace('"', '', regex=False)
df_cleaned.columns = df_cleaned.columns.str.replace('$', '', regex=False)

# Group and simplify columns

df_cleaned["Low Education"] = df_cleaned["No High School Diploma"]
df_cleaned["Medium Education"] = df_cleaned["High School Graduate or GED Certificate"] + df_cleaned["Some College or Tech School"]
df_cleaned["High Education"] = df_cleaned["College Graduate or Post Grad"]

df_cleaned["Low Income"] = df_cleaned["< 20,000"] + df_cleaned["20,000 - 34,999"]
df_cleaned["Medium Income"] = df_cleaned["35,000 - 49,999"] + df_cleaned["50,000 - 74,999"]
df_cleaned["High Income"] = df_cleaned["75,000 - 99,999"] + df_cleaned["100,000+"]

df_cleaned["Young Adult"] = df_cleaned["18 to 34"]
df_cleaned["Middle Aged"] = df_cleaned["35 to 44"] + df_cleaned["45 to 54"]
df_cleaned["Older Adult"] = df_cleaned["55 to 64"] + df_cleaned["65+ years"]

df_cleaned.drop(["No High School Diploma", "High School Graduate or GED Certificate", "Some College or Tech School", "College Graduate or Post Grad",
                "< 20,000", "20,000 - 34,999", "35,000 - 49,999", "50,000 - 74,999", "75,000 - 99,999", "100,000+",
                "18 to 34", "35 to 44", "45 to 54", "55 to 64", "65+ years"], axis = 1, inplace=True)

# Drop unrelated rows
df_cleaned.drop(["White", "Black", "Hispanic", "Asian/Pacific Islander", "Other"], axis = 1, inplace=True)

# Print result and write to csv
with pd.option_context('display.max_rows', 1000, 'display.max_columns', 1000):
    print(df_cleaned)
df_cleaned.to_csv("./data/adult-depression-data-cleaned.csv")

# Summarise dataset
print(f'Describe dataset: \n{df_cleaned.describe()}')
