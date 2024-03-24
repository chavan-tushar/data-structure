# 1. To run a binary search algorithm it is important to have array in a sorted format. 

def find_number(numbers, num) -> int:
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low+high) // 2
        if numbers[mid] == num:
            return mid
        elif num > numbers[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(find_number([2,5,8,9,10, 14, 16, 19], 100))