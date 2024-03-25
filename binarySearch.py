# 1. To run a binary search algorithm it is important to have array in a sorted format. 

def find_number(numbers, num) -> int:
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low+high) // 2
        if numbers[mid] == num:
            if numbers[mid-1] == num:
                high = mid
                continue
            return mid
        elif num > numbers[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(find_number([0,0,0,2,2,2,3,6,6,6,6,6,6,8,8],6))
print(find_number([0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4], 3))