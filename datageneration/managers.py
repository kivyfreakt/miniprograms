from mimesis import Person

person = Person("ru")

string = ''

for _ in range(5):
    string += "( \"" + person.name() + "\" ,\"" + person.surname()+ "\"),"

string = "INSERT INTO managers (name, surname) VALUES " + string +  " ( \"" + person.name() + "\" ,\"" + person.surname()+ "\");"

print(string)