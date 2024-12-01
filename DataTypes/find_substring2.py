c = {}
def find_count(a,b):
    count = 0
    for i in range(len(a) - len(b)+1):
        if a[i:i+len(b)] == b:
            count += 1
    return count

a = "vinayakshayvinayakshayvinayvinaydewarabcdeakshayakshay"
b = ["vinay", "vinaydewar", 'a','akshay']

for i in range(len(b)):
    count = find_count(a,b[i])
    if b[i] not in c:
        c[b[i]] = count
print(c)