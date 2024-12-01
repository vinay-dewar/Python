# """ Data types"""
#
#
# """ STRING data type
#  - it is immutable data type"""
#
# # Checking that the its immutable
#
# a = "test"
# print(id(a))
# a = a+ "vinay"
# print(id(a))
#
# # methods of string
# len(a)   # length in output int
#
#
#
# for i in range(len(a)):
#     print(a[i])
#

#
# a = "0123456789"
# print(a[2:5:2])
# print(a[2:4])
#
#
# """   FIND substring   """
# test = "vinavinay"
#
# a = test.find("vinay")
# print(a)
# b = len("vinay")
# print(b)
# z = test[a:a+b]
# print(z)


def gcd_of_strings(str1, str2):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
            print(a,b)
        return a

    len1 = len(str1)
    len2 = len(str2)
    gcd_length = gcd(len1, len2)
    print(len1, len2, gcd_length)

    def check_common_divisor(s, length):
        divisor = s[:length]
        if divisor * (len(s) // length) == s:
            print(divisor * (len(s) // length))
            return True
        return divisor

    gcd_substring1 = check_common_divisor(str1, gcd_length)

    gcd_substring2 = check_common_divisor(str2, gcd_length)

    if gcd_substring1 and gcd_substring1 == gcd_substring2:
        return gcd_substring1
    return gcd_substring1


# Example usage
str1 = "ABCABCABCDD"
str2 = "ABCABC"
result = gcd_of_strings(str1, str2)
print(f"The GCD of the strings is: '{result}'")
# Output: The GCD of the strings is: 'ABC'
