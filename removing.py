import pandas as pd

data={
    "Name":["Tushar","Aaditya","Himanshu","Manish","Dheeraj","Kunal","dhruv","Aditi"],
    "Age":[23,21,22,25,21,20,26,28],
    "salary":[60000,55000,48000,46000,52000,54000,43000,48000],
    "Performance Score":[95,78,87,86,79,91,83,79]
}
df=pd.DataFrame(data)
print(df)

# droppin a column
df.drop(columns=["Performance Score"],inplace=True)# inplace true means modify the original data/ false gives a new data
print("Modified data")
print(df)