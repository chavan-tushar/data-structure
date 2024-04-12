# def merge(list1, list2):
#     combined = []
#     i = 0
#     j = 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             combined.append(list1[i])
#             i += 1
#         else:
#             combined.append(list2[j])
#             j += 1
#     combined.extend(list1[i:])
#     combined.extend(list2[j:])
#     return combined


def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    combined.extend(list1[i:])
    combined.extend(list2[j:])
    
    return combined


print(merge([],[]))

# def merge_sort(my_list):
#     if len(my_list) == 1:
#         return my_list
    
#     mid = len(my_list) // 2
#     left = merge_sort(my_list[:mid])
#     right = merge_sort(my_list[mid:])

#     return merge(left, right)

# print(merge_sort([1,4,3,2,31, 39, 98,5,6,100,7,9,]))

                