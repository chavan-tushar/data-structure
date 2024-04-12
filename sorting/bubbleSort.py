def bubble_sort(my_list):
    numOfittration = 0
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            numOfittration += 1 
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

    return my_list, numOfittration

print(bubble_sort([100,2,3,4,1,0]))
        