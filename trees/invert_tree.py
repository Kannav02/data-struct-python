from tree import TreeNode

# thinking here is swap the left and the right nodes recursively
def invertTree(root:TreeNode):

    # this will be the base case for the same
    if not root:
        return None
    # this is where the swapping happens between children
    root.left , root.right = root.right, root.left

    # recursive step
    invertTree(root.left)
    invertTree(root.right)