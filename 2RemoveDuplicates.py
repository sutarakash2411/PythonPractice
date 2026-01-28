### Remove duplicates from a list while maintaining order.

my_list = [1, 4, 3, 6, 4, 7, 8, 6, 9, 2, 3, 6, 8, 3, 5]


## below logic has a time complexity of O(n)
new_list = []
for i in range(0, len(my_list), 1):
    if my_list[i] not in new_list:
        new_list.append(my_list[i])
print(new_list) 


## the time complexity can be reduced to O(1) with below code
list2 = []
seen = set()
for num in range(len(my_list)):
    if my_list[num] not in seen:
        list2.append(my_list[num])
        seen.add(my_list[num])
print(list2)

