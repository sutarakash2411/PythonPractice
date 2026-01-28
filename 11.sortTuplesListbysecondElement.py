# Given a list of tuples, sort by second element

def sorttuplelist(lst):
    return sorted(lst, key = lambda x:x[1])
    
myList = [(1,2),(3,6),(6,8),(9,1)]
a = sorttuplelist(myList)
print(a)

#logic 2: using item getter
from operator import itemgetter
def sortedtupleList(lstt):
    return sorted(lstt, key=itemgetter(1))
b = sortedtupleList(myList)
print(b)

#logic3 if to be sorted by first and then second element in case of the elements being same
myList3 = [(1,2),(3,6),(6,8),(9,1),(7,1),(6,3)]
def sortingtuplelist(lis):
    return sorted(lis, key = lambda x:(x[0], x[1]))
obj = sortingtuplelist(myList3)
print(obj)