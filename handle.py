import pandas as pd

#dropna()

data={
    "Name":["Tushar",None,"Himanshu","Manish","Dheeraj","Kunal","dhruv","Aditi"],
    "Age":[23,None,22,25,21,20,26,28],
    "salary":[60000,None,48000,46000,52000,54000,43000,48000],
    "Performance Score":[95,None,87,86,79,91,83,79]
}
df=pd.DataFrame(data)
print(df)

# df.dropna(axis=0,inplace=True)
# print(df)

#fillna(value,inplace=true)

# df.fillna(0,inplace=True)
# print(df)

#we can also use calculated value

df["Age"].fillna(df['Age'].mean(),inplace=True)
print(df)