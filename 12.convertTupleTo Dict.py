# Convert a list of tuples into dictionary

myList = [(1,2),(3,6),(6,8),(9,1),(7,1),(6,3)]
dictionary = dict(myList)
print(dictionary)


#Logic 2: 
dickky = {}
def convertor(lst):
    for key, val in lst:
        dickky[key]= val
    return dickky
a = convertor(myList)
print(a)

#Logic3: if more than 2 elements in tuple
myList3 = [(1,2,54),(3,6,65),(6,8,23),(9,1,87),(7,1,99),(6,3,43)]
dictionary3 = {}
def todict(lst):
    for item in lst:
        dictionary3[item[0]] = item[1:]
    return dictionary3
b = todict(myList3)
print(b)