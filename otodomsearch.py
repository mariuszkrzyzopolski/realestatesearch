from connectclass import Connect
import xlsxwriter

searchlink = [
    "https://www.otodom.pl/sprzedaz/mieszkanie/gdansk/?search%5Bfilter_float_price%3Ato%5D=250000&search%5Bfilter_enum_market%5D%5B0%5D=secondary&search%5Bfilter_float_build_year%3Ato%5D=2016&search%5Bdescription%5D=1&search%5Bdist%5D=10&search%5Bsubregion_id%5D=439&search%5Bcity_id%5D=40&search%5Border%5D=created_at_first%3Adesc",
    "https://www.morizon.pl/mieszkania/najnowsze/gdansk/?ps%5Bprice_to%5D=250000&ps%5Bmarket_type%5D%5B0%5D=2",
    "https://adresowo.pl/mieszkania/gdansk/fuz_p-25_g10_lod",
    "https://www.freedom-nieruchomosci.pl/nieruchomosci?_token=I5jYj5yE5156dTIUxEsw2yyUBlvh7FHTC5HPLvTe&type=OM&trans=S&market=secondary&location=78423&ln=&price_from=50000&price_to=250000&totalArea_from=&totalArea_to=&noOfRooms_from=&noOfRooms_to=&priceM2_from=&priceM2_to=&floorNo_from=&floorNo_to=&noOfFloors_from=&noOfFloors_to=&yearBuilt_from=&yearBuilt_to=&buildingType=&add_date=dowolna&listingId=&agent=&oddzial=",
    "https://metrohouse.pl/na-sprzedaz/mieszkanie/gdansk/-/250000-do_PLN",
]

workbook = xlsxwriter.Workbook('home.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
otodom = Connect(searchlink[0], "a", "listing_no_promo")
otodom.SearchElements("data-featured-name", worksheet, row, col, 2)
col += 1
morizon = Connect(searchlink[1], "a", "property_link")
morizon.SearchElements("class", worksheet, row, col)
col += 1
adresowo = Connect(searchlink[2], "a", "title")
adresowo.SearchElements("class", worksheet, row, col, 1, "https://adresowo.pl")
col += 1
freedom = Connect(searchlink[3], "a", "button brand expanded")
freedom.SearchElements("class", worksheet, row, col)
col +=1
metrohouse = Connect(searchlink[4], "a", "btn btnDarkBlue go_to_prop_btn")
metrohouse.SearchElements("class", worksheet, row, col, 1, "https://metrohouse.pl")

workbook.close()