################# Reverse String ###############################

def reverse_string(str_in):
    reverse = ""
    for i in str_in:
        reverse = i + reverse
    print(reverse)


reverse_string("vij")


def reverse_str(str_in):
    print(str_in[::-1])


reverse_str("vinay")


#################  Factorial  ###############################

def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i

    print(fact)


factorial(1)


def facto(num):
    if num < 2:
        return 1
    else:
        return num * facto(num - 1)


###### find prime number or not

def check_num_is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int((number ** 0.5)) + 1):
        if number % i == 0:
            return False
        else:
            return True


check_num_is_prime(4)  # not prime as it is not it can be divisiable by 2 ,1 and 4


#####print all prime number until the given number

def find_all_prime(num):
    lis = []
    for i in range(2, num + 1):
        if check_num_is_prime(i):
            lis.append(i)
    print(lis)

find_all_prime(7)
