# Authon: Guðjón Ingi Valdimarsson
# Date: 26.03.2020

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
        self.capacity = 5
        self.size = 0
        self.wait = WaitList()

    def add_contact(self, name: str, phone: str, email: str) -> None:
        if self.size == self.capacity:
            self.wait.push((name, phone, email))
        else:
            uid = self.counter
            self.container[uid] = Contact(name, phone, email)
            self.nameContainer[name] = uid
            self.phoneContainer[phone] = uid
            self.emailContainer[email] = uid
            self.counter += 1
            self.size += 1

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
        self.size -= 1
        if len(self.wait) != 0:
            user_input = input("Do you want to add the next one from the queue? (Y/N): ").upper()
            if user_input == "Y":
                contact = self.wait.pop()
                self.add_contact(contact[0], contact[1], contact[2])

    def get_contacts_ordered_by_name(self):
        ordList = []
        for _, cid in self.nameContainer.items():
            ordList.append(self.container[cid])
        return ordList


class WaitList():
    def __init__(self):
        self.front = 0
        self.size = 0
        self.capacity = 8
        self.arr = [None] * self.capacity

    def _resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            new_arr = [None] * self.capacity
            for x in range(self.size):
                arr_index = (self.front + x) % self.size
                new_arr[x] = self.arr[arr_index]
            self.arr = new_arr
            self.front = 0

    def push(self, value):
        self._resize()
        next_index = (self.front + self.size) % self.capacity
        self.arr[next_index] = value
        self.size += 1

    def pop(self):
        ret = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % 8
        self.size -= 1
        return ret
    
    def __len__(self):
        return self.size

if __name__ == "__main__":
    """
    wait = WaitList()
    for x in range(10):
        wait.push(x)
    print (wait.pop())
    print (wait.pop())
    for x in range(10):
        wait.push(x)
    print ()
    """
    contact_list = ContactList()
    contact_list.add_contact("Hanna Hönnudóttir", "1234567", "hanna@hanna.is")
    contact_list.add_contact("Jón Jónsson", "2345678", "jon@jon.is")
    contact_list.add_contact("Anna Önnudóttir", "3456789", "anna@anna.is")
    contact_list.add_contact("Guðmundur Guðmundsson", "4567890", "gummi@gummi.is")
    contact_list.add_contact("Bryndís Bryndísardóttir", "0123456", "disa@disa.is")
    contact_list.add_contact("Mónika Mónikudóttir", "5812345", "mono@mono.is")
    print ()
    contact_list.remove(5)
    print ()