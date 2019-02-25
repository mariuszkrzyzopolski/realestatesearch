from connectclass import Connect
import re



class ConnectResult(Connect):

    # create a parent (in tree) object for search
    def __init__(self, page_link, find, elem_attribute, elem_class):
        self.page_link = page_link
        self.find = find  # tag
        self.elem_attribute = elem_attribute  # attribute
        self.elem_class = elem_class  # attribute value

    # searching for tag inside parent tag and for text without tag
    def search_inside(self, elem_inside, no_class=0, column=0):
        soup = self.CreateStructureSoup()
        value = soup.find(self.find, {self.elem_attribute: self.elem_class})
        result = value.find(elem_inside)
        if not no_class == 0:
            create_patern = ""+no_class+"$"
            patern = re.compile(create_patern)
            a = value.find(text=patern)
            print(a)
            result = a.next_element
            if column == 'morizon':
                result = result.next_element.get_text()
                #need to repair replace
                result = str(result).replace(no_class, '')
                print(result)
                return result
        else:
            result = str(result.get_text())
            return result
