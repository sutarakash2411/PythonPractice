## Find the most frequently repeated element in 

## Logic1 : Wangikarancha Code
myList = [12,32,54,23,54,76,35,23,12,65,24,86,54,23,54,76,35,23,12,65,24,86,12,65,24,86,54,23,54,54,23,54,76,12,65,24,86,12,65,24,86]
myDict = {}
for item in myList:
    count = myList.count(item)
    myDict[item] = count

max_freq = max(myDict.values())

for key, value in myDict.items():
    if value == max_freq:
        print(f"Number {key} has the max Frequency of {value}")



## Logic2: 