#from connectresultclass import ConnectResult
import pandas as pd


def scrapfromresult():
    df = pd.read_csv('results.csv')
    print(df.head())
