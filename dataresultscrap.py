#from connectresultclass import ConnectResult
import pandas as pd


#function for scrap data like price, surface from results.csv
def scrapfromresult():
    df = pd.read_csv('results.csv')
    df.dropna().empty
    for columnsname in df:
        for link in df[columnsname]:
            df.fillna(0, inplace=True)
            if not link == 0:
                if columnsname == 'otodom':
                    print(link)
                    #make a object
