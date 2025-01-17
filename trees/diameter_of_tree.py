from tree import TreeNode


def calculate_diameter(root:TreeNode)-> int :
    global res 
    res = 0

    def dfs(curr:TreeNode):
        if not curr:
            return 0
        
        left = dfs(curr.left)
        right = dfs(curr.right)

        res = max(res,left+right)

        return 1 + max(left,right)
    dfs(root)
    return res