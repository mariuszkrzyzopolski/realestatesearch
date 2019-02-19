#from connectresultclass import ConnectResult
import pandas as pd

#function for scrap data like price, surface from results.csv
def scrapfromresult():
    df = pd.read_csv('results.csv')
    print(df.head())
