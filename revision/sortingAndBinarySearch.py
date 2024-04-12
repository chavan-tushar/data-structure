def find_number(my_list:list, to_find:int) -> int:
    sorted_list = merge_sort(my_list)
    print(sorted_list)
    low = 0
    high = len(sorted_list)
    itr = 0

    while low <= high:
        itr += 1
        mid = (low+high) // 2
        if sorted_list[mid] == to_find:
            return mid, itr
        elif to_find < sorted_list[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1, itr
 
def merge(list1: list, list2: list) -> list:
    combined = []
    i = 0
    j = 0

    while i<len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    combined.extend(list1[i:])
    combined.extend(list2[j:])

    return combined

def merge_sort(my_list: list) -> list:
    if len(my_list) == 1:
        return my_list
    
    mid = len(my_list) // 2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    return merge(left, right)

print(find_number([1,2,3,20,90,10,34,52,69,85,8,7,6,4],52))
