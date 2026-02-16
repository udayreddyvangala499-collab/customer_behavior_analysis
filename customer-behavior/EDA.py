import pandas as pd

df = pd.read_excel('customer_shopping_behavior.xlsx')

# print(df.head())
# print(df.describe(include='all'))
# print(df.info())
# print(df.isnull().sum())
# print(df.columns)
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))
print(df.isnull().sum())
# changing the cols names with snake case => hello_world

df.columns = df.columns.str.lower().str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

# create a column age_group

# print(df['Age'].head())
labels = ['Young Adult', 'Adult', 'Middle Age', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)

# create column purchase_freq_days
# Handling the text data is more complicated than handling the numeric data

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bimonthly': 15,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_freq_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# check whether two cols return same or not

# df['discount_applied'].equals(df['promo_code_used'])  

# since it is true we can remove one col => promo_code_used

df = df.drop('promo_code_used', axis=1)
print(df.columns)

# Download preprocessed dataset
df.to_csv('preprocessed_customer_shopping_behavior.csv', index=False)
print("Preprocessed dataset downloaded as 'preprocessed_customer_shopping_behavior.csv'")