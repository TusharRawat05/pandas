import pandas as pd
data={
    "Name":["Arun","tarun","varun","Karan","Sravan"],
    "Salary":[10000,20000,30000,25000,19000],
    "Age":[28,34,24,28,24]

}
df=pd.DataFrame(data)
grouped=df.groupby("Age")["Salary"].sum()
print(grouped)
