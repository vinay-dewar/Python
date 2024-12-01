fruits = ["apple", "banana", "cherry"]
print(fruits[1:2])  ### banana
fruits[1] = "chikoo"
print(fruits)
fruits.append("apple")
print(fruits)

# list slicing
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lis[2:3])  # [3]

print(lis[-9:-7])  ### [1,2]

print(lis[4:9:3])  ### [5, 8]

print(lis[::-1])  ## all items in reverse

#### list methods

lis1 = [14, 24, 13, 4, 25, 36, 75, 48, 9]

lis1.append(37)  # [1, 2, 3, 4, 5, 6, 7, 8, 9,37]

lis1.remove(7)   # # [1, 2, 3, 4, 5, 6, 8, 9,37]
lis1.pop()
print(lis1)
lis1.reverse()
lis1.insert(1,98765)
print(lis1)

# list comprehension
x = [x for x in range(1, 10)]

print(x)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
