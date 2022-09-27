
class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

rt = node(4)
l,r = node(3), node(5)
ll , lr = node(2) , node(1)
lrl = node(6)
lrr = node(7)

rt.left = l
rt.right = r
l.left = ll
l.right = lr
lr.right = lrr
lr.left = lrl

def left_view(root,lv=0,seen=set()):
    if root is None:
        return
    if lv not in seen:
        print(root.value)
        seen.add(lv)

    left_view(root.right,lv+1,seen)
    left_view(root.left,lv+1,seen)

left_view(rt)
