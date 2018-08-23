import copy as c

#Q1

n = int(input("Enter the number of elements\n"))
print("Enter the elements")
l1 = []
for i in range(n):
    ele = int(input())
    l1.append(ele)
print(l1)
print("Reversed list: ")
l1.reverse()
print(l1)

#Q2

print("enter string")
str1 = input()
final_str = ""
for i in str1:
    if i.isupper():
        final_str = final_str + i
print("characters are: ", final_str)

#Q3

str1 = input("Enter the numbers with commas seperator\n")
l1 = []
l1 = str1.split(",")
print("List : ", l1)

#Q4

print("Enter a string")
str1 = input()
rev = "".join(reversed(str1))
print("str1: ", str1, "rev: ", rev)
if str1 == rev:
    print("String is Palindrome")
else:
    print("String is not Palindrome")

#Q5
# DeepCopy

l1 = [1, 2, [3, 4, 5], 6, 7, 8, 9, 10]
l2 = c.deepcopy(l1)
print('List 1: ', l1)
print('List 2(deepcopy of list 1): ', l2)
l2[2][1] = 11
print('After changing List 2')
print('List 1: ', l1)
print('List 2(deepcopy of list 1): ', l2)
print(" ")

# ShallowCopy

l1 = [1, 2, [3, 4, 5], 6, 7, 8, 9, 10]
l2 = c.copy(l1)
print('List 1: ', l1)
print('List 2(Shallow copy of list 1): ', l2)
l2[2][1] = 11
l2[2][2] = 12
print('After changing List 2')
print('List 1: ', l1)
print('List 2(Shallow copy of list 1): ', l2)

# DIFFERENCE b/w DeepCopy and ShallowCopy.

# Changes made in deep copy of a list are never reflected in the original list where as changes made in shallow copy of a list are always reflected in original list.
# In deepcopy copy of object is copied to other object where as in shallowcopy reference of object is copied in other object
