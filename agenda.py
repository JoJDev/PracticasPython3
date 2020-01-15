import csv


class Contact:

    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):

        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):

        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):

        for idx, contact in enumerate(self._contacts):

            if contact._name.lower() == name.lower():

                del self._contacts[idx]
                print("")
                print("Contacto eliminado".center(50, "="))
                self._save()
                break

    def search(self, name):

        for contact in self._contacts:

            if contact._name.lower() == name.lower():
                self._print_contact(contact)

                break
            else:
                self._not_found()

    def update(self):

        name = str(nput("Escribe el nombre del contacto que quieres actualizar:"))
            
        if self._contacts:

            for contact in self._contacts:
                self._update_option(contact)
                self._save(contact)
                break

    def _save(self):

        with open("contacts.csv", "w") as f:
            writer = csv.writer(f, lineterminator="\r")
            writer.writerow(("name", "phone", "email"))

            for index, contact in enumerate(self._contacts):
                writer.writerow((contact._name, contact._phone, contact._email))
                    

    def _print_contact(self, contact):

        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print("Nombre: {} ".format(contact._name))
        print("Telefono: {} ".format(contact._phone))
        print("Email: {} ".format(contact._email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):

        print("")
        print("El contacto no fue encontrado".center(50, "="))

    def _update_option(self, contact):

        while True:

            name = str(input("Escribe el nuevo nombre del contacto: "))
            phone = str(input("Escribe el nuevo tel del contacto: "))
            email = str(input('Escribe el nuevo email del contacto: '))
            contact._name = name
            contact._phone = phone
            contact._email = email
            print("")
            print("La nueva información del Contacto es: ".center(50, "="))
            self._print_contact(contact)
            break


def run():

    contact_book = ContactBook()
    
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if len(row) == 0:
                continue
            if i == 0:
                continue
            contact_book.add(row[0], row[1], row[2])
    

    while True:

        command = str(input("""
            ¿Que deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contactos
            [b]uscar contacto
            [e]liminar contacto
            [m]ostrar contactos
            [s]alir
        """))

        if command == "a":

            print(" añade tu  contacto ".title().center(70, "="))
            name = str(input("Escribe el nombre de tu contacto: "))
            phone = int(input("Escribe el telefono de "+name + ": "))
            email = str(input("Escribe el e-mail de "+name + ": "))

            contact_book.add(name, phone, email)
            print("")
            print(name + " fue añadido a tus contactos ")

        elif command == "ac":

            print(" actualiza tus contactos ".title().center(70, "="))
            print("")
            contact_book.update()

        elif command == "b":

            print(" busca tus contactos ".title().center(70, "="))
            print("")

            name = str(input("Escribe el nombre del contacto: "))

            contact_book.search(name)

        elif command == "e":

            print(" elimina un contacto ".title().center(70, "="))
            print("")

            name = str(input("Escribe el nombre del contacto: "))

            contact_book.delete(name)

        elif command == "m":

            print(" todos tus contactos ".title().center(70, "="))

            contact_book.show_all()

        elif command == "s":

            break
        else:
            print(" Comando errroneo ".center(50, "="))


if __name__ == "__main__":
    print(" B I E N V E N I D O  A  T U  A G E N D A ".center(70, "="))
    run()