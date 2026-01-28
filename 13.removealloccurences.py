# Remove all occurences of a given element in a list.


num = int(input("provide element"))

#Logic 1
myList = [1,2,3,5,7,6,3,7,8,4,3,5,7,8,9,7,4,3,2,4,5,6,7,7,8,6]
myList = [x for x in myList if x != num]
print(myList)

#Logic 2: 
myList2 = [1,2,3,5,7,6,3,7,8,4,3,5,7,8,9,7,4,3,2,4,5,6,7,7,8,6]
lst=[]
for n in myList2:
    if n != num:
        lst.append(n)  
print(lst)


#Logic 3 !!!!!!!!!!!!Erroneous result!!!!!!
# since this code update the list while iterating thro same list, and if the num is present consecutively, 
# then later num's index position is moved to earlier and gets skipped
myList3 = [1,2,3,5,7,6,3,7,8,4,3,5,7,8,9,7,4,3,2,4,5,6,7,7,8,6]
for item in myList3:
    if item is num:
        myList3.remove(item)
print(myList3)

