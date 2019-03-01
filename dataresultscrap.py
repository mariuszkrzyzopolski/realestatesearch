from connectresultclass import ConnectResult
import pandas as pd


#function for scrap data like price, surface from results.csv
def scrapfromresult():
    result_list = {'source': [], 'price': [], 'surface': [], 'floor': [], 'build_year': [], 'heating': [], 'rent': []}
    df = pd.read_csv('results.csv')
    df.fillna(0, inplace=True)
    result_list = pd.DataFrame(data=result_list)
    for columnsname in df:
        for link in df[columnsname]:
            if not link == 0:
                if columnsname == 'otodom':
                    continue
                    #problem with scrap from otodom.suspend
                    #price = ConnectResult(link, "li", "class", "param_price").search_inside('strong')
                    #surface = ConnectResult(link, "li", "class", "param_m").search_inside('strong')
                    #floor = ConnectResult(link, "li", "class", "param_floor_no").search_inside('strong')
                    #build_year = ConnectResult(link, "ul", "class", "sub-list").search_inside('strong', "Rok budowy:")
                    #heating = ConnectResult(link, "ul", "class", "sub-list").search_inside('strong', "Ogrzewanie:")
                    #rent = ConnectResult(link, "ul", "class", "sub-list").search_inside('strong', "Czynsz:")
                elif columnsname == 'morizon':
                    price = ConnectResult(link, "li", "class", "paramIconPrice").search_inside('em')
                    surface = ConnectResult(link, "li", "class", "paramIconLivingArea").search_inside('em')
                    floor = ConnectResult(link, "section", "class", "params clearfix").search_inside('th', "Piętro: ",columnsname)
                    build_year = ConnectResult(link, "section", "class", "params clearfix").search_inside('th', "Rok budowy: ",columnsname)
                    heating = ConnectResult(link, "section", "class", "params clearfix").search_inside('h3', "Ogrzewanie",columnsname)
                    rent = None
                elif columnsname == 'adresowo':
                    price = ConnectResult(link, "span", "class", "price").search_inside('', '', 'default')#dosent search
                    surface = ConnectResult(link, "div", "id", "offer-summary").search_inside('', " o powierzchni ")#return tag, should text
                    floor = ConnectResult(link, "div", "id", "offer-summary").search_inside('b', "piętro", columnsname)
                    build_year = None
                    heating = None
                    #heating = ConnectResult(link, "div", "id", "offer-description").search_inside('br', " Ogrzewanie")
                    rent = None
                elif columnsname == 'freedom':
                    price = ConnectResult(link, "div", "class", "columns large-5").search_inside('span')
                    surface = ConnectResult(link, "div", "class", "columns large-12 data").search_inside("ul" ,'pow. całkowita',"freedom")
                    floor = ConnectResult(link, "div", "class", "small-12 data").search_inside("div","piętro","freedom")
                    build_year = None
                    heating = None
                    rent = None
                elif columnsname == 'metrohouse':
                    price = ConnectResult(link, "div", "itemprop", "offers").search_inside("span")
                    surface = ConnectResult(link, "div", "class", "table-responsive").search_inside("span")
                    floor = ConnectResult(link,"div","class","table-box-style").search_inside('div',0,columnsname,18)
                    build_year = ConnectResult(link, "div", "class", "table-responsive").search_inside("span",0,columnsname,4)
                    heating = ConnectResult(link,"div","class","table-box-style").search_inside('div',0,columnsname,40)
                    rent = ConnectResult(link,"div","class","table-box-style").search_inside('div',0,columnsname,37)
                result_list = savescrap(result_list, link, price, surface, floor, build_year, heating, rent)
    result_list.to_csv('info.csv', index=False)


def savescrap(result_list, link, price, surface, floor=None, build_year=None, heating=None, rent=None):
    tmp_dict = {'source': [link], 'price': [price], 'surface': [surface], 'floor': [floor], 'build_year': [build_year], 'heating': [heating], 'rent': [rent]}
    tmp_dict = pd.DataFrame(tmp_dict)
    result_list = pd.concat([result_list, tmp_dict])

    return result_list


#only for testing
scrapfromresult()