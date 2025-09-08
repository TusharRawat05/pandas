import pandas as pd

df=pd.read_json("sample_data.json")

print("displaying the info of the data Set")
print(df.info())