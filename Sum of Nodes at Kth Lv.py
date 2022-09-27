
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

def sum_kth_lv(root,k,lv=1):
    store = [[root,lv]]
    sum_lv = 0
    while len(store) > 0:
        root_t , level = store[0]
        if root_t is not None:
            if level == k:
                sum_lv += root_t.value
            store.append([root_t.left,level+1])
            store.append([root_t.right ,level+1])
        store.pop(0)
    return sum_lv

print(sum_kth_lv(root1,4))