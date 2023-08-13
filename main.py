from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value


class Name:
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class Record:
    def __init__(self, name, phones):
        self.name = name
        self.phones = [phones]

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass


class AddressBook(UserDict):
    def add_record(self, record: Record):
        # self.data[record.value] = record
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get[value]


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')
