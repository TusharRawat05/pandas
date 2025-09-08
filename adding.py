import pandas as pd

data={
    "Name":["Tushar","Aaditya","Himanshu","Manish","Dheeraj","Kunal","dhruv","Aditi"],
    "Age":[23,21,22,25,21,20,26,28],
    "salary":[60000,55000,48000,46000,52000,54000,43000,48000],
    "Performance Score":[95,78,87,86,79,91,83,79]
}
df=pd.DataFrame(data)

print(df)
#square bracket df["Column name"]=some_data
df["Bonus"]=df["salary"]*0.1
print("data frame with new cloumn Bonus")
print(df)

#using insert()
#df.insert(loc,"column_name",some_data)
df.insert(0,"Employee Id",[10,20,30,40,50,60,70,80])
print("new Column inserted Employee ID")
print(df)