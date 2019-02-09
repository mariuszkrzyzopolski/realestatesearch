from connectclass import Connect
from bs4 import BeautifulSoup

searchlink = "https://www.otodom.pl/sprzedaz/mieszkanie/gdansk/?search%5Bfilter_float_price%3Ato%5D=250000&search%5Bfilter_enum_market%5D%5B0%5D=secondary&search%5Bfilter_float_build_year%3Ato%5D=2016&search%5Bdescription%5D=1&search%5Bdist%5D=10&search%5Bsubregion_id%5D=439&search%5Bcity_id%5D=40&search%5Border%5D=created_at_first%3Adesc"

otodom = Connect(searchlink, "a", "listing_no_promo")
page_response = otodom.LinkConnection()
soup = BeautifulSoup(page_response.content, 'html.parser')
links = soup.find_all(otodom.find, {"data-featured-name" : otodom.elem_class})

for otodom.find in links:
    print("Found the URL:", otodom.find['href'])
