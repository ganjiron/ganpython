from PythonClass.HW import BinarySearchTree


class BSTMain:
    def __init__(self):
        pass

    def main(self):
        bst = BinarySearchTree.BinarySearchTree()
        input_data = (17, 5, 25, 2, 11, 29, 38, 9, 16, 7, 8)
        for i in input_data:
            bst.put(i, i)
        bst.root.inorder_traverse()
        print('remove 5')
        bst.delete(5)
        bst.root.inorder_traverse()
        print('put 39')
        bst.put(39, 39)
        bst.root.inorder_traverse()


if __name__ == '__main__':
    bstApp = BSTMain()
    bstApp.main()
