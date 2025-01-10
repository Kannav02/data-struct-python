
class TreeNode:

    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    


def search(root,val):

# 4 cases
    if not root: #not found
        return False

    if root.val < val : # move to the right
        return search(root.right,val)
    elif root.val > val: # move to the left
        return search(root.left,val)
    else:
        return True # found the element

