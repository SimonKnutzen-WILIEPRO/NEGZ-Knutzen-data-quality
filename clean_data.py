import pandas as pd

df = pd.read_csv("sample_data_with_errors_first_corr.csv", sep=";")
print(df)
print(df.info())

df = df.drop_duplicates()

id_counts = df['id'].groupby(df['id']).count()
print(id_counts[id_counts > 1])
# Replace '/' with '.' in date_of_birth

for id in id_counts[id_counts > 1].index:
    print(f"Duplicate ID: {id}")
    for i in range(id_counts[id] - 1):
        row_idx = df[df['id'] == id].index[i+1]
        df.loc[row_idx, 'id'] = df['id'].max() + 1

df['date_of_birth'] = df['date_of_birth'].str.replace('/', '.', regex=False)

df['salary'] = df['salary'].str.replace(' EUR', '', regex=False).str.replace(',', '.', regex=False)
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df['is_active'] = df['is_active'].str.strip().str.lower().map({'true': True, 'false': False, '1': True, '0': False, 'yes': True, 'no': False})


print(df)

# Keep original strings for fallback parsing
dob_original = df['date_of_birth'].copy()

# Primary pass: YYYY-MM-DD style
df['date_of_birth'] = pd.to_datetime(dob_original, dayfirst=False, errors='coerce')

# Fallback pass: try dayfirst=True for DD.MM.YYYY / DD/MM/YYYY style
mask = df['date_of_birth'].isna()
df.loc[mask, 'date_of_birth'] = pd.to_datetime(dob_original[mask], dayfirst=True, errors='coerce')

df = df[df['salary'].notna() & (df['salary'] > 0) & (df['salary'] != 999999.99)]

print(df)
print(df.info())

df_new = pd.read_json("additional_entries.json")
df = pd.concat([df, df_new], ignore_index=True)

id_counts = df['id'].groupby(df['id']).count()
print(id_counts[id_counts > 1])
# Replace '/' with '.' in date_of_birth

for id in id_counts[id_counts > 1].index:
    print(f"Duplicate ID: {id}")
    for i in range(id_counts[id] - 1):
        row_idx = df[df['id'] == id].index[i+1]
        df.loc[row_idx, 'id'] = df['id'].max() + 1

print(df)