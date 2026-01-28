## Merge two sorted lists into one sorted list

list1 = [12,32,54,37,53,86,26,97,46,85,35,23]
list2 = [21,32,54,34,66,24,65,36,32,76,35,67]

sorted1 = list(sorted(list1))   #sorting list1
sorted2 = list(sorted(list2))   #sorting list2

merged = sorted1 + sorted2      #Merging two sorted lists
mergedSorted = sorted(merged)   #sorting merged list
print("Simpleway: ", mergedSorted)
#######################################################################################
def mergeSortedLists(l1,l2):
    i = j = 0
    mergedList = []
    while i < (len(sorted1)) and j < (len(sorted2)):
        if sorted1[i] < sorted2[j]:
            mergedList.append(sorted1[i])
            i += 1
        else:
            mergedList.append(sorted2[j])
            j += 1
    return mergedList
uniqueList=mergeSortedLists(list1,list2) 
print("Merged list using method: ", uniqueList)
    

