strr = "abcdefghi"
substring = "fgh"
def find_substring(strr,substring):
    for i in range(len(strr) - len(substring) + 1):
        count = 0
        if strr[i:i+ len(substring)] == substring:

            return True

    return False

print(find_substring(strr,substring))

##############################
# FIND sublist


a,b = [1, 1, 1, 2, 3, 4, 5, 5, 6], [5, 5, 6]

def find_sublist(a,b):
    for i in range(len(a) - len(b) +1 ):
            if b == a[i: i + len(b)]:
                return True
    return False
print(find_sublist(a,b))