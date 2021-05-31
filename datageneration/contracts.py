from mimesis import Person, Business, Text, Datetime
from random import randint
import datetime
person = Person("ru")
business = Business("ru")
text = Text("ru")
time = Datetime("ru")

string = ''

for _ in range(200):
    a = time.date()
    b = time.date()
    if (a > b):
        b, a = a, b
    string += "( \"Описание\" , " + str(randint(1000, 1000000))+ ", " + str(randint(2, 43)) + ", " + str(randint(1,10)) + ", DATE(\"" + str(a) + "\"), DATE(\"" + str(b) + "\"), " + str(randint(0,1)) + "),"

string = "INSERT INTO contracts (description, price, client_id, manager_id, begin, end, is_end) VALUES " + string + "( \"Описание\" , " + str(randint(1000, 1000000))+ ", " + str(randint(2, 43)) + ", " + str(randint(1,10)) + ", DATE(\"" + str(a) + "\"), DATE(\"" + str(b) + "\"), " + str(randint(0,1)) + ");"
print(string)
