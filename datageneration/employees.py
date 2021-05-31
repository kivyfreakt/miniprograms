from mimesis import Person
from random import randint
person = Person("ru")

string = ''

for _ in range(134):
    string += "( \"" + person.name() + "\" ,\"" + person.surname()+ "\", " + str(randint(1, 45)) + ", " + str(randint(1, 6)) + "),"

string = "INSERT INTO employees (name, surname, exp, specialisation_id) VALUES " + string +  "( \"" + person.name() + "\" ,\"" + person.surname()+ "\", " + str(randint(1, 45)) + ", " + str(randint(1, 6)) + ");"

print(string)