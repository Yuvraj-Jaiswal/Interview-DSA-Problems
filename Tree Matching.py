
class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

root1 = node(4)
l,r = node(3), node(5)
ll , lr = node(2) , node(1)
lrl = node(6)
lrr = node(7)

root1.left = l
root1.right = r
l.left = ll
l.right = lr
lr.right = lrr
lr.left = lrl

root2 = node(1)
root2.left = node(6)
root2.right = node(7)

def tree_matching(root1,root2):
    if root1 is None:
        return

    if root1.value == root2.value:
        return is_match(root1,root2)

    mat_l = tree_matching(root1.left,root2)
    mat_r = tree_matching(root1.right,root2)

    if mat_l is True or mat_r is True:
        return True
    else:return False


def is_match(root_1,root_2):
    if root_1 is None and root_2 is None:
        return True
    if root_1 is None and root_2 is not None:
        return False
    if root_1 is not None and root_2 is None:
        return False
    if root_1 is not None and root_2 is not None:
        if root_1.value == root_2.value:
            return is_match(root_1.left,root_2.left) and is_match(root_1.right,root_2.right)
        else:
            return False


print(tree_matching(root1,root2))