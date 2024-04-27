# Heap is similar to Binary search tree. The only difference between binary search tree and heap is each node has value greater than or equal to all its decendents. 
# That means the highest value will be at the top which is also known as max heap. 
# We can have a min heap as well. Which means minimum value at the top and every node will have less than or equal to value than all its decendents. 
# A heap is a complete tree. Which means all the nodes are filled from left to right direction with no spaces in between. 
# A heap can have a duplicate value.
# A heap is stored in a list format. the first element of list will be root and then left child and right child which are present in next level. After adding all the nodes of current level the nodes which are present in its next level are stored in a list
# How to find a child of a given node ?
#     if Nodes are stored in a list from index number starting from 1. 
#         Left child - 
#             The left child a node which is at index 'n' is calculated by 2 * n 
#         Right child - 
#             The right child of a node which is at index 'n' is calculated by (2 * n) + 1

#     if Nodes are stored in a list from index number starting from 0
#         Left Child - 
#             (2 * n) + 1
#         right child -
#             (2 * n) + 2
        
# How to find a parent of a given node ?
#     In case of a list which holds the data from index 1
#         To find a parent divide the node's index by 2. 
#     In case of list which holds the data from index 0
#         index - 1 // 2
    