# Find all pairs in a list that sum up to a given target

# targetSum = 6

# finalList = []
# def targetSumPairs(lst):
#     list1 = []
#     for num in lst:
#         remainder = targetSum - num
#         if remainder in lst and remainder != num:
#             list1.append((num,remainder))
#             #list1.append(num)
#             #list1.append(remainder)
#             finalList.append(list1)
#     return list1

# mylist = [1,2,3,4,5,6,7,8,9,11,12,14,13,15,16,17,18,19,20]
# a = targetSumPairs(mylist)
# print(a)





def possiblePairsSum(my_list, target):
    final_list = []
    for num in my_list:
        complement = target - num
        if complement in my_list and complement != num:
            temp_list = list()
            temp_list.append(num)
            temp_list.append(complement)
            final_list.append(temp_list)
    return final_list

input_list = [2, 3, 4, 7, 5, 1]
target_sum = 6
pairs = possiblePairsSum(input_list, target_sum)
print(pairs)




























