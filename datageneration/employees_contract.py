from random import randint

string = ''

for _ in range(399):
    string += "(" + str(randint(6, 206)) + " , " +  str(randint(7, 142))+ "),"

string = "INSERT INTO employees_contracts (contracts_id, workers_id) VALUES " + string + "(" + str(randint(6, 206)) + " , " +  str(randint(7, 142))+ ");"
print(string)
