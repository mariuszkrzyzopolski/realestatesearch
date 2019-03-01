from connectclass import Connect
import bs4
import re



class ConnectResult(Connect):

    # create a parent (in tree) object for search
    def __init__(self, page_link, find, attribute, elem_class):
        self.page_link = page_link
        self.find = find  # tag
        self.attribute = attribute  # attribute
        self.elem_class = elem_class  # attribute value

    # searching for tag inside parent tag and for text without tag
    def search_inside(self, elem_inside, no_class=0, column=0, next=0):
        soup = self.CreateStructureSoup()
        value = soup.find(self.find, {self.attribute: self.elem_class})
        result = value.find(elem_inside)
        if not no_class == 0:
            create_patern = ""+no_class+"$"
            patern = re.compile(create_patern)
            a = value.find(text=patern)
            print(a)
            if a is None:
                return None
            if column == 'adresowo':
                return a
            result = a.next_element
            if column == 'morizon':
                result = result.next_element.get_text()
                no_class = "\n"+no_class+"\n"
                result = str(result).replace(no_class, '')
                result = str(result).replace("\n", '')
            if column == 'freedom':
                return result.get_text()
            return result.get_text()
        else:
            if column == 'metrohouse':
                result = value.find_all(elem_inside)
                result = result[next]
            result = str(result.get_text())
            print(result)
            return result
