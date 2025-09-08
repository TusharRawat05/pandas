import pandas as pd


#NaN(not a number)
#None(for object datatype)
'''
isnull()
true-value is missing
false-value is not missing 
'''
data={
    "Name":["Tushar",None,"Himanshu","Manish","Dheeraj","Kunal","dhruv","Aditi"],
    "Age":[23,None,22,25,21,20,26,28],
    "salary":[60000,None,48000,46000,52000,54000,43000,48000],
    "Performance Score":[95,None,87,86,79,91,83,79]
}
df=pd.DataFrame(data)

print(df)
print(df.isnull()) # give complete data with true and false
print(df.isnull().sum())# gives the number of evry missing value 