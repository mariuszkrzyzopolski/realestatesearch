import requests


class Connect:
    def __init__(self, page_link, find, elem_class):
        self.page_link = page_link
        self.find = find
        self.elem_class = elem_class

    def linkConnection(self):
        return requests.get(self.page_link, timeout=5)

