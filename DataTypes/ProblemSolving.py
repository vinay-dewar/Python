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


################# Find max number in list ###########################

def find_max_num(lis):
    max_num = lis[0]
    for i in range(1, len(lis)):
        if lis[i] > max_num:
            max_num = lis[i]
    print("vin")
    print(max_num)


find_max_num([3, 3, 3, 2, 2, 67, 2, 3, 87, 4, 5, 5, 3])


# 2
def find_max_number(lis):
    new = sorted(lis)
    print(f" this is max : {new[-1]}")


find_max_number([3, 3, 3, 2, 2, 67, 2, 3, 87, 4, 5, 5, 3])


#####################Find Duplicates and count in dict as key value##################
#  [3,3,32,32,2,67,2,87,87,4,5,5,3]
def find_count_of_duplicates(lis):
    unique = []
    count = {}
    for i in range(len(lis)):
        if lis[i] not in unique:
            unique.append(lis[i])
    for x in range(len(unique)):
        print(f" The count of {unique[x]} is {lis.count(unique[x])}")
        count[unique[x]] = lis.count(unique[x])
    print(count)


find_count_of_duplicates([3, 3, 32, 32, 2, 67, 2, 87, 87, 4, 5, 5, 3])


### without use of count

def find_duplicates_add_count_in_dict(lis):
    dic = {}
    for i in range(len(lis)):
        if lis[i] in dic:
            dic[lis[i]] += 1
        else:
            dic[lis[i]] = 1
    print(dic)


find_duplicates_add_count_in_dict([3, 3, 32, 32, 2, 67, 2, 87, 87, 4, 5, 5, 3])


#### sort list

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]


##### fibonacchi
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        print(fib)


print(fibonacci(15))


###########Check the string is alphnumeric
# true if alnum
# false if not alnum

def is_alnum(s):
    for charr in s:
        if not ((charr >= 'a' and charr <= 'z') or (charr >= 'A' and charr <= 'Z') or (charr >= '0' and charr <= '9')):
            return False
        else:
            return True

######### merge two string ulternate

def merge_alternatively(list1, list2):
    merged_list = []
    len1, len2 = len(list1), len(list2)

    for i in range(max(len1, len2)):
        if i < len1:
            merged_list.append(list1[i])
        if i < len2:
            merged_list.append(list2[i])

    return merged_list


# Example usage
list1 = ['a', 'b', 'c']
list2 = ['x', 'y', 'z']
merged = merge_alternatively(list1, list2)
print("Merged List:", merged)  # Output: ['a', 'x', 'b', 'y', 'c', 'z']


# find GCD of numers

a,b = 10,20

while b != 0:
    a,b = b, a%b
    print(a,b)
print(a)

########## Find count of vovels in the string also add seprate count in the dict
A = "aaeioqerfevdnh"
vovels = ['a','e','i','o','u']
total_count = 0
seprate_count = {}
for i in A:
    if i in vovels:
        total_count += 1
        if i not in seprate_count:
            seprate_count[i] = 1
        else:
            seprate_count[i] += 1
print(total_count)
print(seprate_count)


######### FIND the largerst two digit in the integer

a = 998989876767
b = str(a)
largest = None
for i in range(len(b)):
    two_digit_no = int(b[i:i+2])
    if largest is None or two_digit_no > largest:

        largest = two_digit_no
print(largest)

# find fibo
a = [0,1]
while len(a) < 10:
    a.append(a[-1]+a[-2])
print(a)

a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,11]
b = a[:2]
while len(b) < len(a):
    b.append(b[-1]+b[-2])
print(b)
if a==b:
    print(True)
else: print(False)


### find longest palidrome

def is_palidrome(s):
    return s == s[::-1]

longest_pali = ""

def get_logest_palidrome(sttr):
    for i in range(len(sttr)):
        for j in range(i,len(sttr)):
            sub = sttr[i:j+1]
            print(sub)
