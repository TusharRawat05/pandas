import pandas as pd

data={
    "Name":['Ram','Mohan','shyam','Tushar'],
    "Age":[12,20,20,30,],
    "city":['Nagpur','Mumbai','Delhi','gurgaon']
}

df=pd.DataFrame(data)

print(df)
# df.to_csv("output.csv",index=False) #without index
# df.to_excel("output.xlsx",index=False)
df.to_json("output.json")