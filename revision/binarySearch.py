
def check_num(to_find, my_list):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low+high) // 2
        if my_list[mid] == to_find:
            if my_list[mid-1] == to_find:
                high = mid
                continue
            return mid
        elif to_find < my_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(check_num(70, [1,2,3,4,5,6,7,8,9]))

    # low = 0
    # high = len(numbers) - 1

    # while low <= high:
    #     mid = (low+high) // 2
    #     if numbers[mid] == num:
    #         if numbers[mid-1] == num:
    #             high = mid
    #             continue
    #         return mid
    #     elif num > numbers[mid]:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    # return -1

