import pandas as pd

data={
    "Name":["Tushar","Aaditya","Himanshu","Manish","Dheeraj","Kunal","dhruv","Aditi"],
    "Age":[23,21,22,25,21,20,26,28],
    "salary":[60000,55000,48000,46000,52000,54000,43000,48000],
    "Performance Score":[95,78,87,86,79,91,83,79]
}
df=pd.DataFrame(data)
print(df)
#single Column
print("names(single column return series)")
print(df["Name"])

#Multiple Cloumn
print("multiple Cloumn")
subset=df[["Name","salary"]]
print(subset)

# for rows
High_salary=df[df['salary']>50000]
print("More than 50k salary")
print(High_salary)

#filtering rows salary>45k and age 23+
filtered=df[(df['salary']>45000) &(df['Age']>23)]
print(filtered)

# we can also use or
new_filter=df[(df['salary']>52000) | (df['Performance Score']>82)]
print(new_filter)