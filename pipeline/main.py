import pandas as pd
import os

print("Current working directory:", os.getcwd())
# Since data.csv is in the same directory as main.py
df = pd.read_csv("./pipeline/data.csv")

def shape(df):
    return df.shape[0] # row should be 2

print(shape(df))
