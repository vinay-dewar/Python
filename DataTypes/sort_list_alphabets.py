a = [3,75,3,56,8,4,33]

for i in range(len(a)-1):
    for j in range(i,len(a)-1):
        if a[i] > a[j+1]:
            a[i], a[j + 1] = a[j+1], a[i]


print(a[-1])
print(a)