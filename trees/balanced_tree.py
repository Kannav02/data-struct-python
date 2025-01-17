from tree import TreeNode




def balanced_tree(root):

    def dfs(curr):
        if not curr:
            return [True,0]
        
        left = dfs(curr.left)
        right = dfs(curr.right)
        balanced = (left[0] and right[0]) and abs(left[1]-right[1] <= 1)

        return [balanced,1+max(left,right)]

    return dfs(root)[1]
