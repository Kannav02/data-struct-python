from tree import TreeNode

def calculate_depth(root:TreeNode):
    if not root:
        return 0
    
    return 1+max(calculate_depth(root.left),calculate_depth(root.right))