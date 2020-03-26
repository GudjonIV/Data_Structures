# Author: Guðjón Ingi Valdimarsson
# Date: 24.03.2020

from sortedcollections import SortedDict

class Contact():
    def __init__(self, nameStr: str, phoneStr: str, emailStr: str) -> None:
        self.nameStr = nameStr
        self.phoneStr = phoneStr
        self.emailStr = emailStr

class ContactList():
    def __init__(self):
        self.container = {}
        self.nameContainer = SortedDict()
        self.phoneContainer = {}
        self.emailContainer = {}
        self.counter = 1

    def add_contact(self, name: str, phone: str, email: str) -> None:
        uid = self.counter
        self.container[uid] = Contact(name, phone, email)
        self.nameContainer[name] = uid
        self.phoneContainer[phone] = uid
        self.emailContainer[email] = uid
        self.counter += 1

    def get_by_name(self, name: str) -> Contact:
        cid = self.nameContainer[name]
        return self.container[cid]

    def get_by_phone(self, phone: str) -> Contact:
        cid = self.phoneContainer[phone]
        return self.container[cid]
    
    def get_by_email(self, email: str) -> Contact:
        cid = self.emailContainer[email]
        return self.container[cid]

    def get_by_id(self, cid: int) -> Contact:
        return self.container[cid]
    
    def remove(self, cid) -> None:
        contact = self.container[cid]
        del self.nameContainer[contact.nameStr]
        del self.phoneContainer[contact.phoneStr]
        del self.emailContainer[contact.emailStr]
        del self.container[cid]

    def get_contacts_ordered_by_name(self):
        ordList = []
        for _, cid in self.nameContainer.items():
            ordList.append(self.container[cid])
        return ordList

if __name__ == "__main__":
    contact_list = ContactList()
    contact_list.add_contact("Hanna Hönnudóttir", "1234567", "hanna@hanna.is")
    contact_list.add_contact("Jón Jónsson", "2345678", "jon@jon.is")
    contact_list.add_contact("Anna Önnudóttir", "3456789", "anna@anna.is")
    contact_list.add_contact("Guðmundur Guðmundsson", "4567890", "gummi@gummi.is")
    contact_list.add_contact("Bryndís Bryndísardóttir", "0123456", "disa@disa.is")
    some_contact_1 = contact_list.get_by_name("Anna Önnudóttir")
    some_contact_2 = contact_list.get_by_phone("4567890")
    some_contact_3 = contact_list.get_by_email("hanna@hanna.is")
    ordered_contact_list = contact_list.get_contacts_ordered_by_name()
    for contact in ordered_contact_list:
        print(contact.nameStr)
    
    print ("--------Testing remove--------")
    contact_list.remove(4)
    ordered_contact_list = contact_list.get_contacts_ordered_by_name()
    for contact in ordered_contact_list:
        print(contact.nameStr)

