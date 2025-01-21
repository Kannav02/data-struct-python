from tree import TreeNode
from collections import deque

def inorder(root):
    stack = []
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            curr= curr.right

def preorder(root):
    stack = []
    curr = root

    while curr or stack:
        if curr:
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

def postorder(root):
    # still todo
    pass

def bfs(root):
    queue = deque(([root]))

    while queue:
        current = queue.popleft()
        print(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        
