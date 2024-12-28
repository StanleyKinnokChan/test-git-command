import pandas as pd
import pytest

df = pd.read_csv(r"C:\Users\StanleyChan\SynologyDrive\Tech\python\Pytest\pipeline\data.csv")

def shape(df):
    return df.shape[0] # row should be 2
