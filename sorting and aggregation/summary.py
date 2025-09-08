#numerical summary
'''
df["column Name"].sum()
df["column"].min()
df["cloumn"].max()
'''

import pandas as pd

data={
    "Name":["Arun","tarun","varun"],
    "Salary":[10000,20000,30000],
    "Age":[28,34,22]

}
df=pd.DataFrame(data)
avg_salary=df["Salary"].mean()
print(avg_salary)