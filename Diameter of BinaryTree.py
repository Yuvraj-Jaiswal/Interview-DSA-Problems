
class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

rt = node(6)
l,r = node(2), node(1)
lr = node(3)
lrr = node(4)
rr = node(5)

    #     6
    # 2       1
    #     3      5
    #         4

rt.left = l
rt.right = r
l.right = lr
lr.right = lrr
r.right = rr

def diameter(root,ht=0):
    if root is None:
        return ht
    hl = diameter(root.left,ht+1)
    hr = diameter(root.right,ht+1)
    return max(hl,hr)


print(diameter(rt))

# will do it later