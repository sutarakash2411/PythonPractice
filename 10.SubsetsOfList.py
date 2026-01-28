# Given a list, print all possible subsets of that list

def subsets(lst):
    subset = [[]]
    for item in lst:
        subset += [i + [item] for i in subset ]
    for val in subset:
        print(val)
    print(f"Length: {len(subset)}")
    return
mylist = [ 1, 2, 3, 4,5]
a = subsets(mylist)
 