
def find_max_2_digit(b,digit):
    max = int(b[:digit])

    for i in range(1,len(b)):
        if int(b[i:i+digit]) > max:
            max = int(b[i:i+digit])
    return max
a = find_max_2_digit("123999456789",3)
print(a)
