from connectclass import Connect


class ConnectResult(Connect):
    # create a parent (in tree) object for search
    def __init__(self, page_link, find, elem_attribute, elem_class):
        self.page_link = page_link
        self.find = find  # tag
        self.elem_attribute = elem_attribute  # attribute
        self.elem_class = elem_class  # attribute value

    # searching for tag inside parent tag and for text without tag
    def search_inside(self, elem_inside, no_class=0):
        soup = self.CreateStructureSoup()
        value = soup.find(self.find, {self.elem_attribute: self.elem_class})
        result = value.find(elem_inside)
        # maybe rebuild it with find or find_all ? read bs4 documentation a loop is too heavy
        if not no_class == 0:
            results = value.find_all(elem_inside)
            for a in results:
                b = a
                a = a.get_text()
                print(a)
                if a == no_class:
                    result = b.next_sibling
                    return result
        else:
            result = str(result.get_text())
            return result
