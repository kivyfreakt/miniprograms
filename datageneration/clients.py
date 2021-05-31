from mimesis import Person, Business
from random import randint
person = Person("ru")
business = Business("ru")

string = ''

for _ in range(40):
    string += "( \"" + person.name() + "\" ,\"" + person.surname()+ "\", \"" + business.company() + "\"),"

string = "INSERT INTO clients (name, surname, company) VALUES " + string + "( \"" + person.name() + "\" ,\"" + person.surname()+ "\", \"" + business.company() + "\");"
print(string)
