from connectclass import Connect
from bs4 import BeautifulSoup
import xlsxwriter


searchlink = "https://www.otodom.pl/sprzedaz/mieszkanie/gdansk/?search%5Bfilter_float_price%3Ato%5D=250000&search%5Bfilter_enum_market%5D%5B0%5D=secondary&search%5Bfilter_float_build_year%3Ato%5D=2016&search%5Bdescription%5D=1&search%5Bdist%5D=10&search%5Bsubregion_id%5D=439&search%5Bcity_id%5D=40&search%5Border%5D=created_at_first%3Adesc"

workbook = xlsxwriter.Workbook('home.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
i = 1
otodom = Connect(searchlink, "a", "listing_no_promo")
page_response = otodom.LinkConnection()
soup = BeautifulSoup(page_response.content, 'html.parser')
links = soup.find_all(otodom.find, {"data-featured-name" : otodom.elem_class})

for otodom.find in links:
    if i%2 == 0:
        worksheet.write(row, col, otodom.find['href'])
        row += 1
    i += 1

workbook.close()