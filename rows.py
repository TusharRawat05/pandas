import pandas as pd
df=pd.read_json("sample_data.json")

print("Display 10 rows of first")
print(df.head(10))

print("Display 10 rows of last")
print(df.tail(10))

# if we dont pass any number in head and tail it will give 5
# by this we can check data is loaded or not from first to last