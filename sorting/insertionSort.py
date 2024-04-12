def insertionSort(my_list):
    for i in range(1, len(my_list)):
            temp = my_list[i]
            j = i-1
            while temp < my_list[j] and j > -1:
                noOfitloop2 += 1
                my_list[j+1], my_list[j] = my_list[j], temp
                j -= 1
    return my_list

print(insertionSort([0, 10, 88, 11, 7, 100,2,4,3,5,6]))