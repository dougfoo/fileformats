import pandas as pd
import csv

df_mf = pd.read_csv("baby-names.csv")
df_mf = df_mf.drop(columns=["year","percent"]).drop_duplicates()
df_mf["name"] = df_mf["name"].apply(lambda x: x.upper())
df_mf["sex"].replace({'boy':'M','girl':'F'}, inplace=True)
print(df_mf.head())

df = pd.read_csv("chicago-salary.csv")
df[["Lname","Fname"]] = df["Name"].str.split(',',expand=True)
df["Fname"] = df["Fname"].str.strip().str.split(" ").str[0]
df.dropna(subset=["Annual Salary"], inplace=True)
df["Annual Salary"] = df["Annual Salary"].astype(int)
print(df.head())
 
df_gender = df.merge(df_mf, 'left', left_on='Fname', right_on='name').drop(columns=["name"])
df_gender["sex"].fillna("?", inplace=True )
df_gender.rename(columns={"sex":"gender","Job Titles":"jobtitle","Annual Salary":"salary","Department":"department","Fname":"fname","Lname":"lname"}, inplace=True)
df_gender = df_gender[["fname","lname","department","jobtitle","gender","salary"]]
print(df_gender.head())

df_gender.to_csv("chicago-salary-gender.csv", index_label="id", quoting=csv.QUOTE_NONNUMERIC, header=False)
df_gender.T.to_csv("chicago-salary-gender_col.csv", index_label="id", quoting=csv.QUOTE_NONNUMERIC, header=False, )
df_gender.to_json("chicago-salary-gender.json", orient="records" )
df_gender.to_parquet("chicago-salary-gender.parq")

