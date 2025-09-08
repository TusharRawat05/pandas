'''
vertically(row-wise)
horizontally(column-wise)

pd.concate([df1,df2],axis=0,ignore_index=True)
'''

#vertically
import pandas as pd

#region
df_Region1=pd.DataFrame({
    "CustomerId":[1,2],
    "Name":["Gopal","Raju"]
})

#region 2

df_Region2=pd.DataFrame({
    "CustomerId":[3,4],
    "Name":["Shyam","Baburao"]
})

#concate vertically
df_concat=pd.concat([df_Region1,df_Region2],ignore_index=True)
print(df_concat)