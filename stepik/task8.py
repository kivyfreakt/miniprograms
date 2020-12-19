n = int(input())
pruf = list(map(int, input().split()))
leafes = []
for i in range(1, n+3): # для курса исправить диапазон
    if i not in pruf:
        leafes.append(i)

while pruf != []:
    x = pruf.pop(0)
    y = leafes.pop(0)
    if x > y:
        print(y, x)
    else:
        print(x, y)
    if x not in pruf:
        leafes.append(x)
    leafes.sort()
print(min(leafes), max(leafes))
