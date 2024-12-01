a  = 53
b = [22, 23, 30, 10, 49,  24]
c,d = b[0], b[1]
for i in range(len(b)):
    for j in range(i,len(b)):
        if b[i] + b[j]  == a or b[i] + b[j] == a-1 or b[i] + b[j] == a+1:
            # print(b[i],  b[j])
            c,d = b[i], b[j]
print(c,d)