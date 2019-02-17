import requests
from bs4 import BeautifulSoup


class Connect:
    def __init__(self, page_link, find, elem_class):
        self.page_link = page_link
        self.find = find
        self.elem_class = elem_class

    @property
    def LinkConnection(self):
        return requests.get(self.page_link, timeout=5)

    def CreateStructureSoup(self):
        soup = self.LinkConnection
        return BeautifulSoup(soup.content, 'html.parser')

    def SearchElements(self, searched, j=1, add=""):
        soup = self.CreateStructureSoup()
        links = soup.find_all(self.find, {searched: self.elem_class})
        i = 1
        row = 0
        listlinks = []
        for self.find in links:
            if i % j == 0:
                listlinks.append(add+self.find['href'])
                row += 1
            i += 1
            if row == 25:
                break
        return listlinks