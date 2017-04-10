class ContactList():
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        ContactList.all_contacts.append(self)

    def match(self,name):
        matching_contacts=[]
        for contact in ContactList.all_contacts:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

    def search(self,name):
        match= self.match(name)
        for item in match:
            print(item.name,item.email)


class Supplier(ContactList):

    def order(self, order):
        print("{} is in need from {}".format(order, self.name))


if __name__ == '__main__':
    c = ContactList('eddie', 'eddy_gg@163.com')
    s = Supplier('harvey', 'harvey@google.com')
    s.order('Google Glasses')
    s.search('eddie')
