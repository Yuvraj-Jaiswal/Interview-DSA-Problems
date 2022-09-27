
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

#          4
#      3       5
#  2      1
#      6     7


rt.left = l
rt.right = r
l.right = lr
lr.right = lrr
r.right = rr


def top_view(root_g):
    stack = [[root_g,0]]
    seen = set()
    while len(stack) > 0:
        root , hw = stack[0][0] , stack[0][1]

        if hw not in seen:
            seen.add(hw)
            print(root.value, end=" ")

        if root.left: stack.append([root.left,hw-1])
        if root.right: stack.append([root.right,hw+1])
        stack.pop(0)


top_view(rt)