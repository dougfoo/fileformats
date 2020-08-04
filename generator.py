import pandas as pd
import sys

df = pd.read_csv("chicago-salary.csv")
df_mf = pd.read_csv("baby-names.csv")
df_mf.drop(columns=["year","percent"], inplace=True)
df_mf.drop_duplicates(inplace=True)
df_mf["name"] = df_mf["name"].apply(lambda x: x.upper())
df_mf["sex"].replace({'boy':'M','girl':'F'}, inplace=True)

df[["Lname","Fname"]] = df["Name"].str.split(',',expand=True)
df["Fname"] = df["Fname"].str.strip().str.split(" ").str[0]
df.drop(columns=["Name","Full or Part-Time","Hourly Rate","Typical Hours","Salary or Hourly"], inplace=True)
df.dropna(subset=["Annual Salary"], inplace=True)
print(df.head())
 
df_gender = df.merge(df_mf, 'left', left_on='Fname', right_on='name').drop(columns=["name"])
df_gender["sex"].fillna("?", inplace=True )
df_gender.rename(columns={"sex":"Gender","Job Titles":"Title","Annual Salary":"Salary"}, inplace=True)

print(df_gender.head())
print(df_gender.size) 

df_gender.to_csv("chicago-salary-gender.csv")
df_gender.to_json("chicago-salary-gender.json", orient="records" )
df_gender.to_parquet("chicago-salary-gender.parq")

