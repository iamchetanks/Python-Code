class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
#global root
def inserttree(root, new_val):

    if root[0] == None:
        root[0] = Node(new_val)
        return
    if new_val < root[0].value:
        if root[0].left == None:
            root[0].left = Node(new_val)
            return
        else:
            inserttree([root[0].left], new_val)
            return
    else:
        if root[0].right == None:
            root[0].right = Node(new_val)
            return
        else:
            inserttree([root[0].right], new_val)
            return

def inorder(root):
    if root[0] is not None:
        inorder([root[0].left])
        print(root[0].value, end=" ")
        inorder([root[0].right])
def preorder(root):
    if root[0] is not None:
        print(root[0].value, end=" ")
        preorder([root[0].left])
        preorder([root[0].right])

def postorder(root):
    if root[0] is not None:
        postorder([root[0].left])
        postorder([root[0].right])
        print(root[0].value, end=" ")


a = [1,0,2,3,4,-1,5]
root = [None]
for i in a:

    inserttree(root, i)
print("inorder")
inorder(root)
print("preorder")
preorder(root)
print("postorder")
postorder(root)


