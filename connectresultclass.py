from connectclass import Connect


class ConnectResult(Connect):
    def __init__(self, page_link, find, elem_attribute, elem_class):
        self.page_link = page_link
        self.find = find
        self.elem_attribute = elem_attribute
        self.elem_class = elem_class

    def search_inside(self, elem_inside, no_class=0):
        soup = self.CreateStructureSoup()
        value = soup.find(self.find, {self.elem_attribute: self.elem_class})
        result = value.find(elem_inside)
        if not no_class == 0:
            results = value.find_all(elem_inside)
            for a in results:
                b = a
                a = a.get_text()
                if a == no_class:
                    result = b.next_sibling
                    #problem with detecting NaN value
                    if result == 'Rynek:':
                        result = "NaN"
                    return result
        return result.get_text()
