import pandas as pd

#sorting data 1 column sort_values()
# true=ascending false=descending

data={
    "Name":["Arun","tarun","varun"],
    "Salary":[10000,20000,30000],
    "Age":[28,34,22]

}
df=pd.DataFrame(data)
df.sort_values(by="Age",ascending=False,inplace=True)
print("sorted age by descending order")
print(df)

# for Multiple value
df.sort_values(by=["Age","Salary" ],ascending=[True,False],inplace=True)
print(df)