a = "abccdcdabcdcba"
pali = ""

def is_pali(s):
    if s == s[::-1]:
        return True
for i in range(len(a)):
    for j in range(i,len(a)):
        if is_pali(a[i:j+1]) and len(a[i:j+1]) > len(pali):
            pali = a[i:j+1]
            print(pali)
print(pali)