import datetime          #importing datetime module

class Person:            #Defining class
    def __init__(self, name, surname, birthday, address, telephone, email): # Special method to pass class obects
        self.name = name 
        self.surname = surname
        self.birthday = birthday

        self.address = address
        self.telephone = telephone
        self.email = email 

    def age(self):   #Defining a function
        today = datetime.date.today()
        age = today.year - self.birthday.year

        if today < datetime.date(today.year, self.birthday.month, self.birthday.day):
            age -= 1

            return age

person = Person(
    'Jane',
    'Doe',
    datetime.date(1992,2,12),
    'No 12 Short Street Seattle',
    '555 456 789',
    'jane.doe@example.com'
)

print(person.name)
print(person.email)
print(person.age())


