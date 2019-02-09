from bs4 import BeautifulSoup
from connectclass import Connect

searchlink = "https://www.otodom.pl/sprzedaz/mieszkanie/gdansk/?search%5Bfilter_float_price%3Ato%5D=250000&search%5Bfilter_enum_market%5D%5B0%5D=secondary&search%5Bfilter_float_build_year%3Ato%5D=2016&search%5Bdescription%5D=1&search%5Bdist%5D=10&search%5Bsubregion_id%5D=439&search%5Bcity_id%5D=40&search%5Border%5D=created_at_first%3Adesc"

otodom = Connect(searchlink, "a", "offer-item-title")
page_response = otodom.linkConnection()
soup = BeautifulSoup(page_response.content, 'html.parser')
links = soup.find_all(otodom.find, href=True)

for a in links:

    if a.find_all("span", class_=otodom.elem_class, limit=1):
            print("Found the URL:", a['href'])
