from timeit import default_timer as timer

RED = 'RED'
BLACK = 'BLACK'


class Node:
    def __init__(self, key):
        self.key = key
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None

    def get(self):
        return self.key

    def set(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if (self.left != None):
            children.append(self.left)
        if (self.right != None):
            children.append(self.right)
        return children


class RB:
    def __init__(self):
        nil_node = Node(0)
        nil_node.color = BLACK
        self.NIL = nil_node
        self.root = self.NIL

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insertFixup(self, z):
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.leftRotate(z)

                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.rightRotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rightRotate(z)

                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.leftRotate(z.parent.parent)

        self.root.color = BLACK

    def insert(self, k):
        y = self.NIL
        x = self.root
        z=Node(k)
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.right = self.NIL
        z.left = self.NIL
        z.color = RED

        self.insertFixup(z)

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if (currentNode == self.NIL):
            return False
        elif (key == currentNode.key):
            return True
        elif (key < currentNode.key):
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)

    def inorder(self, n):
        if n != self.NIL:
            self.inorder(n.left)
            print(n.key, n.color)
            self.inorder(n.right)

