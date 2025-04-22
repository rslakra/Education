#
# Author: Rohtash Lakra
#
import pandas as pd
from pathlib import Path

data = [
    {
        "id": "dcadcde83b95496a87ff26b9416e9f6e",
        "make": "Acura",
        "model": "CL",
        "year": "1996",
        "enabled": 0
    },
    {
        "id": "4243d593aac24b308130a1a7e250a435",
        "make": "Acura",
        "model": "CL",
        "year": "1996",
        "enabled": 0
    },
    {
        "id": "48dd1c109a814c23b96d9f9eafdb5507",
        "make": "Acura",
        "model": "CL",
        "year": "1997",
        "enabled": 0
    },
    {
        "id": "d93e382293e54272a6475994b0decef8",
        "make": "Acura",
        "model": "CL",
        "year": "1997",
        "enabled": 0
    },
    {
        "id": "91eb4bd163c44b4db33a57ebd99cce27",
        "make": "Acura",
        "model": "CL",
        "year": "1998",
        "enabled": 0
    }
]

print(f"data={data}")
print()

# Working
# pd = pd.DataFrame(data)
# print('Build DataFrame only with data')
# print(pd)

# Not Working
# pd = pd.DataFrame(data=data, index=[1])
# print('Build DataFrame only with index')
# print(pd)

# Working
# COLUMN_NAMES=['id', 'make', 'model', 'year', 'enabled']
# pd = pd.DataFrame(data=data, columns=COLUMN_NAMES)
# print('Build DataFrame with columns')
# print(pd)

# Not Working
# COLUMN_NAMES=['id', 'make', 'model', 'year', 'enabled']
# DATA_TYPES={'id': str, 'make': str, 'model': str, 'year': int, 'enabled': bool}
# pd = pd.DataFrame(data=data, dtype=DATA_TYPES)
# print('Build DataFrame with columns')
# print(pd)

# pd = pd.DataFrame(data=data, columns=['id', 'make', 'model', 'year', 'enabled'], dtype=)
# print('Build DataFrame with columns')
# print(pd)

# pd = pd.DataFrame(data, index=0,
#                   columns=['id', 'make', 'model', 'year', 'enabled'],
#                   dtype={'id': str, 'make': str, 'model': str, 'year': int, 'enabled': bool})
# print(f"pd={pd}")
print()


vehicles=[{'id': 'dcadcde83b95496a87ff26b9416e9f6e', 'make_id': 'b04965e6a9bb591f8f8a1adcb2c8dc39', 'make': 'Acura', 'model_id': '3f1c1ff9110d53109b33af01e1e86a53', 'model': 'CL', 'year': '1996', 'enabled': 0}, {'id': '4243d593aac24b308130a1a7e250a435', 'make_id': 'b04965e6a9bb591f8f8a1adcb2c8dc39', 'make': 'Acura', 'model_id': '3f1c1ff9110d53109b33af01e1e86a53', 'model': 'CL', 'year': '1996', 'enabled': 0}, {'id': '48dd1c109a814c23b96d9f9eafdb5507', 'make_id': 'b04965e6a9bb591f8f8a1adcb2c8dc39', 'make': 'Acura', 'model_id': '3f1c1ff9110d53109b33af01e1e86a53', 'model': 'CL', 'year': '1997', 'enabled': 0}, {'id': 'd93e382293e54272a6475994b0decef8', 'make_id': 'b04965e6a9bb591f8f8a1adcb2c8dc39', 'make': 'Acura', 'model_id': '3f1c1ff9110d53109b33af01e1e86a53', 'model': 'CL', 'year': '1997', 'enabled': 0}, {'id': '91eb4bd163c44b4db33a57ebd99cce27', 'make_id': 'b04965e6a9bb591f8f8a1adcb2c8dc39', 'make': 'Acura', 'model_id': '3f1c1ff9110d53109b33af01e1e86a53', 'model': 'CL', 'year': '1998', 'enabled': 0}]
# pd = pd.DataFrame(existing_vehicles)
COLUMN_NAMES=['id', 'make', 'model', 'year', 'enabled']
df = pd.DataFrame(data=vehicles, columns=COLUMN_NAMES)
DATA_TYPES={'id': str, 'make_id': str, 'make': str, 'model_id': str, 'model': str,'year': int, 'enabled': bool}
# pd = pd.DataFrame(data=existing_vehicles, columns=COLUMN_NAMES, dtype=DATA_TYPES)
print('Build DataFrame only with data')
print(df)
print("Apply lowercase to make")
df['make_lowercase'] = df['make'].apply(lambda x: str(x).lower())
print("Apply lowercase to model")
df['model_lowercase'] = df['model'].apply(lambda x: str(x).lower())
print("Apply lowercase to year")
df['year'] = (df['year'].apply(lambda x: str(x).lower() if str(x).lower() != 'nan' else ''))

print("'id'\t'make'\t'model'\t'year'\t'enabled'")
# iterate each record of DataFrame
for index, row in df.iterrows():
    print(f"index={index}, row={row['id'], row['make'], row['model'], row['year'], row['enabled']}")

print()
curr_dir = Path(__file__).parent
data_file_path = curr_dir.joinpath('vehicle.csv')
print(f"data_file_path={data_file_path}")
csv_df = pd.read_csv(data_file_path, dtype=str, encoding='utf8', delimiter=';')
print(csv_df)
