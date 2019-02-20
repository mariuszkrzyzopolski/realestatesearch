from connectresultclass import ConnectResult
import pandas as pd


#function for scrap data like price, surface from results.csv
def scrapfromresult():
    result_list = {'source': [], 'price': [], 'surface': [], 'floor': [], 'build_year': []}
    df = pd.read_csv('results.csv')
    for columnsname in df:
        for link in df[columnsname]:
            df.fillna(0, inplace=True)
            if not link == 0:
                if columnsname == 'otodom':
                    #do others properies
                    price = ConnectResult(link, "li", "class", "param_price").search_inside('strong')
                    surface = ConnectResult(link, "li", "class", "param_m").search_inside('strong')
                    floor = ConnectResult(link, "li", "class", "param_floor_no").search_inside('strong')
                    build_year = ConnectResult(link, "ul", "class", "sub-list").search_inside('strong', "Rok budowy:")
                    #do a function to save that!!!
                    result_list['source'].append(link)
                    result_list['price'].append(price)
                    result_list['surface'].append(surface)
                    result_list['floor'].append(floor)
                    result_list['build_year'].append(build_year)
        result_list = pd.DataFrame(data=result_list)
        result_list.to_csv('info.csv', index=False)
