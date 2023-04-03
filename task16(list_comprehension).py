# 1. WAP on List Comprehension by using if condition.
# Print even no. in a new list from old list.

# old list that is numbers which is even and odd no.
num = [34,23,41,24,76,21,89,56,99,14,]

# new list that is even which is only even
# from old list.

even  = [x for x in num if x % 2 == 0]
print(even)
# OUTPUT : [34, 24, 76, 56, 14]

# WAP on List Comprehension normal way
# without condition

food = ["ice-cream","burger","shake","pizza","pasta"]
new_list = [x.upper() for x in food]
print(new_list)
# OUTPUT : ['ICE-CREAM', 'BURGER', 'SHAKE', 'PIZZA', 'PASTA']


