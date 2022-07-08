
def solution(info, edges):
    answer = 0
    node = array_to_bst(info, 0)
    # print(node.data)]
    preorder(node)
    return answer


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    print(node.data)
    if node.left!= None:
        preorder(node.left)
    if node.right!=None:
        preorder(node.right)
    
def array_to_bst(nums,head):
    node = Node(nums[head])
    
    left = pow(2, head)
    right = pow(2, head)+1
    if left<len(nums):
        node.left = Node(left)
        array_to_bst(nums, left)
    if right<len(nums):
        node.right = Node(right)
        array_to_bst(nums, right)

    return node