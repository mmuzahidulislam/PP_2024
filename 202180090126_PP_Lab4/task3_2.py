import pandas as pd

pd.options.display.float_format = '{:.2f}'.format
df = pd.read_csv('grades-126.csv')

df['Average'] = df[['exam1', 'exam2', 'exam3']].mean(axis=1)

# Create a new DataFrame row for the class averages
avg_row = pd.DataFrame({
    'firstname': ['Class Average'],
    'lastname': [''],
    'exam1': df['exam1'].mean(),
    'exam2': df['exam2'].mean(),
    'exam3': df['exam3'].mean()
})

df = pd.concat([df, avg_row], ignore_index=True)
print(df)
