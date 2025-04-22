#
# Author: Rohtash Lakra
#

data = {
    "make": [
        "Acura",
        "BMW",
        "Acura",
        "Acura",
        "Audi",
        "Studebaker",
        "Packard",
        "Audi",
        "Packard",
        "BMW"
    ],
    "model": [
        "CL",
        "02 (E10)",
        "CSX",
        "CL",
        "Quattro",
        "Commander",
        "120",
        "Quattro",
        "Twelve",
        "02 (E10)"
    ],
    "year": [
        "1996",
        "1996",
        "2006",
        "1996",
        "1991",
        "1954",
        "1935",
        "1991",
        "1936",
        "1996"
    ]
}

df = pd.DataFrame(data)
print(df)
unique_values = df.stack().unique()
print(unique_values)
duplicated = df.duplicated()
print(duplicated)
duplicated_df = df[duplicated]
print(duplicated_df)
# Remove the row with index 1
duplicated_df = duplicated_df.drop(1)
print(duplicated_df)

