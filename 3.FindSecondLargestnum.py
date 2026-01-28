## Find second largest number in a list

my_list = [12,45,54,63,26,74,38,27,27,22,32,74,39  ]

largest = secondLargest = float('-inf')
if len(my_list) < 2:
    print("List length not sufficient.")

else:
    for num in my_list:
        if num > largest:
            secondLargest = largest
            largest = num 
        elif num > secondLargest:
            secondLargest = num

print("secondLargest Numberis: ", secondLargest)