# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs_preord(node, res_str):
            # base case
            # result is a string with separater , and None, i.e.: '1,2,3,None,None,4,None,None,5,None,None'
            if not node:
                res_str += 'None,'
            else:
                res_str += str(node.val) + ','
                res_str = dfs_preord(node.left, res_str)
                res_str = dfs_preord(node.right, res_str)
            return res_str
    
        return dfs_preord(root, '')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs_preord_reverse(res_str_lst):
            # base case
            if res_str_lst[0] == 'None':
                # pop first element
                res_str_lst.pop(0)
                return None
            # pop every element as node
            node = TreeNode(res_str_lst[0])
            res_str_lst.pop(0)
            
            node.left = dfs_preord_reverse(res_str_lst)
            node.right = dfs_preord_reverse(res_str_lst)
            return node
        
        # use a list instead of a string...
        res_str_lst = data.split(',')
        root = dfs_preord_reverse(res_str_lst)
        return root
        
        
                
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
