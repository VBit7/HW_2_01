from AddressBook import *


class Command:
    def execute(self, bot):
        pass


class AddCommand(Command):
    def execute(self, bot):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        bot.book.add(record)

        # name = Name(input("Name: ")).value.strip()
        # phones = Phone().value
        # birth = Birthday().value
        # email = Email().value.strip()
        # status = Status().value.strip()
        # note = Note(input("Note: ")).value
        # record = Record(name, phones, birth, email, status, note)
        # return self.book.add(record)
        

class SearchCommand(Command):
    def execute(self, bot):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = bot.book.search(pattern, category)
        birth = ''
        print('This is SearchBot()')
        print(result)
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
            result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
            print(result)

        # print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        # category = input('Search category: ')
        # pattern = input('Search pattern: ')
        # result = (self.book.search(pattern, category))
        # for account in result:
        #     if account['birthday']:
        #         birth = account['birthday'].strftime("%d/%m/%Y")
        #         result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
        #         print(result)



class EditCommand(Command):
    def execute(self, bot):
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        bot.book.edit(contact_name, parameter, new_value)

        # contact_name = input('Contact name: ')
        # parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        # new_value = input("New Value: ")
        # return self.book.edit(contact_name, parameter, new_value)


class RemoveCommand(Command):
    def execute(self, bot):
        pattern = input("Remove (contact name or phone): ")
        bot.book.remove(pattern)

        # pattern = input("Remove (contact name or phone): ")
        # return self.book.remove(pattern)


class SaveCommand(Command):
    def execute(self, bot):
        file_name = input("File name: ")
        bot.book.save(file_name)

        # file_name = input("File name: ")
        # return self.book.save(file_name)


class LoadCommand(Command):
    def execute(self, bot):
        file_name = input("File name: ")
        bot.book.load(file_name)

        # file_name = input("File name: ")
        # return self.book.load(file_name)


class CongratulateCommand(Command):
    def execute(self, bot):
        print(bot.book.congratulate())

        # print(self.book.congratulate())


class ViewCommand(Command):
    def execute(self, bot):
        print(bot.book)

        # print(self.book)


class ExitCommand(Command):
    def execute(self, bot):
        pass


class Bot:
    def __init__(self):
        self.book = AddressBook()
        self.commands = {
            'add': AddCommand(),
            'search': SearchCommand(),
            'edit': EditCommand(),
            'remove': RemoveCommand(),
            'save': SaveCommand(),
            'load': LoadCommand(),
            'congratulate': CongratulateCommand(),
            'view': ViewCommand(),
            'exit': ExitCommand(),
        }

    def handle(self, action):
        if action in self.commands:
            self.commands[action].execute(self)
        else:
            print("There is no such command!")


"""


# Приклад використання:
bot = Bot()
bot.handle('add')
bot.handle('search')
# ... і так далі
"""


"""
class AddBot(AbstractBot):
    def handle(self):
        record = self.create_record()
        return self.book.add(record)

    def create_record(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        return record


class SearchBot(AbstractBot):
    def handle(self):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = self.book.search(pattern, category)
        self.dispaly_result(result)

    def dispaly_result(self, result):
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)
"""

"""
class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        if action == 'add':
            name = Name(input("Name: ")).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(input("Note: ")).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = input('Search category: ')
            pattern = input('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    print(result)
        elif action == 'edit':
            contact_name = input('Contact name: ')
            parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = input("Remove (contact name or phone): ")
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = input("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            print(self.book.congratulate())
        elif action == 'view':
            print(self.book)
        elif action == 'exit':
            pass
        else:
            print("There is no such command!")
"""