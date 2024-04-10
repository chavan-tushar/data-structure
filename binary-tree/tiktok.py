def find_number(numbers, num) -> int:
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low+high) // 2
        if numbers[mid-1] == num:
            high = mid
            continue
        elif numbers[mid] == num:
            return mid
        else:
            low = mid + 1
    return -1

print(find_number(["g","g","g","b","b"],"b"))
