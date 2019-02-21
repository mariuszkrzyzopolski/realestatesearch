from connectresultclass import ConnectResult
import pandas as pd


#function for scrap data like price, surface from results.csv
def scrapfromresult():
    result_list = {'source': [], 'price': [], 'surface': [], 'floor': [], 'build_year': [], 'heating': [], 'rent': []}
    df = pd.read_csv('results.csv')
    for columnsname in df:
        for link in df[columnsname]:
            df.fillna(0, inplace=True)
            if not link == 0:
                if columnsname == 'otodom':
                    price = ConnectResult(link, "li", "class", "param_price").search_inside('strong')
                    surface = ConnectResult(link, "li", "class", "param_m").search_inside('strong')
                    floor = ConnectResult(link, "li", "class", "param_floor_no").search_inside('strong')
                    build_year = ConnectResult(link, "ul", "class", "sub-list").search_inside('strong', "Rok budowy:")
                    heating = ConnectResult(link, "ul", "class", "sub-list").search_inside('strong', "Ogrzewanie:")
                    rent = ConnectResult(link, "ul", "class", "sub-list").search_inside('strong', "Czynsz:")
                result_list = savescrap(result_list, link, price, surface, floor, build_year, heating, rent)
            elif columnsname == 'morizon':
                #values for morizon
        result_list = pd.DataFrame(data=result_list)
        result_list.to_csv('info.csv', index=False)


def savescrap(result_list, link, price, surface, floor='NaN', build_year='NaN', heating='NaN', rent='NaN'):
    result_list['source'].append(link)
    result_list['price'].append(price)
    result_list['surface'].append(surface)
    result_list['floor'].append(floor)
    result_list['build_year'].append(build_year)
    result_list['heating'].append(heating)
    result_list['rent'].append(rent)
    return result_list