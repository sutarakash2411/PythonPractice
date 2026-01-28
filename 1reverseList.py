####### Reverse a given list without using builtin reverse methods

list =[1, 2, 3, 4, 5]
print(list)

##    logic 1
rev_list = []
for i in range(0,len(list), 1):
    rev_list.append(list[-i-1])
print(rev_list)

##  Logic 2
secondRevList=[]
for i in range(len(list)-1, -1, -1):
    secondRevList.append(list[i])
print(secondRevList)

