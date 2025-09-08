import pandas as pd

data={
    "Name":["Tushar","Aaditya","Himanshu","Manish","Dheeraj","Kunal","dhruv","Aditi"],
    "Age":[23,21,22,25,21,20,26,28],
    "salary":[60000,55000,48000,46000,52000,54000,43000,48000],
    "Performance Score":[95,78,87,86,79,91,83,79]
}
df=pd.DataFrame(data)
print("before updating")
print(df)
df.loc[0,"salary"]=75000 # for specfic one
print("after updating")
print(df)

#increase salary by 5%
print(" salary increment by 5%")
df["salary"]=df["salary"]*1.05
print(df)