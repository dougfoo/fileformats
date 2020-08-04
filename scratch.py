import pandas as pd
import sys

df = pd.read_csv("chicago-salary.csv")

print(df["Name"].split(",").head())


