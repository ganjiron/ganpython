class TreeNode:

    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent


    def hasLeftChild(self):
        return self.leftChild != None
    def hasRightChild(self):
        return self.rightChild != None
    def isLeftChild(self):
        # 부모가 있으면 내가 부모의 왼쪽인지 체크
        if self.parent != None:
            return self.parent.leftChild == self
        else:
            return False

    def isRightChild(self):
        # 부모가 있으면 내가 부모의 오른쪽인지 체크
        if self.parent != None:
            return self.parent.rightChild == self
        else:
            return False
    def isRoot(self):
        return self.parent == None
    def isLeaf(self):
        return self.rightChild == None or self.leftChild == None
    def hasAnyChildren(self):
        return self.rightChild != None or self.leftChild != None
    def hasBothChildren(self):
        return self.rightChild != None and self.leftChild != None
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        if self.isLeaf():
            return None
        if self.hasRightChild():
            return self.rightChild.findMin()
        elif not self.isRoot() and self.hasLeftChild():
            return self.parent
    def findMin(self):
        if self.hasLeftChild():
            return self.leftChild.findMin()
        else:
            return self

    def sliceOut(self):
        if self.parent and self.hasRightChild():
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
    def inorder_traverse(self):
        if self.hasLeftChild():
            self.leftChild.inorder_traverse()
        print(self.payload)
        if self.hasRightChild():
            self.rightChild.inorder_traverse()

