#pd.merge(df1,df2, on="cloumn_name",how="type of join")
import pandas as pd

#customer dataframe

df_customers=pd.DataFrame({
    'Customer Id':[1,2,3],
    'Name':['Ramesh','Suresh','Kalpesh']
})
#order dataframe

df_order=pd.DataFrame({
    "Customer Id":[1,2,4],
    'OrderAmount':[250,450,350]
})
#mergex
df_merge1=pd.merge(df_customers,df_order,on="Customer Id",how="inner")
print("inner Join")
print(df_merge1)

df_merge2=pd.merge(df_customers,df_order,on="Customer Id",how="outer")
print("outer Join")
print(df_merge2)

df_merge3=pd.merge(df_customers,df_order,on="Customer Id",how="left")
print("left Join")
print(df_merge3)

df_merge4=pd.merge(df_customers,df_order,on="Customer Id",how="right")
print("right Join")
print(df_merge4)

