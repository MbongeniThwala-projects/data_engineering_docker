import sys

import pandas as pd

print('arguments', sys.argv)
#we normally have parameters to our pipeline eg processing month 12
month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month

#saving our data processing to parquet
df.to_parquet(f"output_{month}.parquet")

print(df.head())
print(f'Laying Pipe, month={month}')