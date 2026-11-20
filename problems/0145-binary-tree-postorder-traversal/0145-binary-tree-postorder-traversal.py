class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)   # <-- moved to the end

        dfs(root)
        return result