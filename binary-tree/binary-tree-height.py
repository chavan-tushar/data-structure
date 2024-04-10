class TreeNode():
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.right = None
        self.left = None

def create_binary_tree(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = create_binary_tree(data[0])
        node.right = create_binary_tree(data[1])
    elif data == None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree_tuple = ((None,9,None),3,(15,20,7))
tree = create_binary_tree(tree_tuple)

class Solution:
    def helper(self, root):
        print(root)
        if root is None:
            return 0
        leftValue = self.helper(root.left)
        rightValue = self.helper(root.right)

        if leftValue == -1 or rightValue == -1:
            return -1
        
        if abs(leftValue - rightValue) > 1:
            return -1
        
        return 1 + max(leftValue, rightValue)

    def isBalanced(self, root) -> bool:
        # print(root.left.val)
        answer = self.helper(root)
        if answer != -1:
            return True
        return False

    
s1 = Solution()
print(s1.isBalanced(tree))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        



