import pandas as pd
data={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}
df=pd.DataFrame(data)
print("before interpolation")
print(df)

print("after interpolation")
# df.interpolate(method="linear",axis=0,inplace=True)
df["Value"]=df["Value"].interpolate(method="linear")
print(df)

'''
when to use
1-time series data
2-numeric data with trends 
3-avoid dropping rows
'''