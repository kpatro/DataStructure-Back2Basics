class BinarySearchTree:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def add_child(self, par):
        if self.value == par:
            return  # node already exists
        # traverse right
        if par > self.value:
            if self.right:
                self.right.add_child(par=par)
            else:
                self.right = BinarySearchTree(par)

        # traverse left
        elif self.value > par:
            if self.left:
                self.left.add_child(par=par)
            else:
                self.left = BinarySearchTree(par)

    def search(self, ele):
        if self.value == ele:
            return True
        elif ele > self.value:
            if self.right:
                return self.right.search(ele)
        elif ele < self.value:
            if self.left:
                return self.left.search(ele)
            return False

    # Depth First Traversal Technique
    def pre_order_traversal(self):
        # root -> left -> right
        elements = [self.value]
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
        return elements

    def post_order_traversal(self):
        # left -> right -> root
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.value)
        return elements

    def in_order_traversal(self):
        # Left -> Root -> Right
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        elements.append(self.value)
        if self.right:
            elements += self.right.post_order_traversal()
        return elements

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.value

    def find_min(self):
        if self.left:
            return self.left.find_max()
        return self.value

    def delete(self, val):
        """
        deleting data from tree can be done 2 ways
        find min of right subtree beneath the node to be deleted and replace that with the node deleted
        or
        find max of left subtree beneath the node deleted and replace it with max value
        """
        if val > self.value:
            if self.right:
                self.right = self.right.delete(val)
        elif val < self.value:
            if self.left:
                self.left = self.left.delete(val)
        else:
            if self.right is None and self.left is None:
                return

            min_val = self.find_min()
            self.value = min_val
            self.right = self.right.delete(min_val)

            # max_value = self.find_max()
            # self.value = max_value
            # self.left = self.left.delete(max_value)
        return self


def build_binary_tree(bt_elements):
    print("Building Binary Tree")
    root = BinarySearchTree(bt_elements[0])

    for i in bt_elements:
        root.add_child(i)

    return root


if __name__ == '__main__':
    pass

    # nt = build_binary_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # print("In order traversal gives this sorted list:", nt.in_order_traversal())
    # print("Pre order traversal gives this sorted list:", nt.pre_order_traversal())
    # print("Post order traversal gives this sorted list:", nt.post_order_traversal())
    # nt.delete(val=23)
    # print("After Deleting 23:", nt.in_order_traversal())
    # nt.delete(val=1)
    # print("After Deleting 1:", nt.in_order_traversal())
    # nt.delete(val=17)
    # print("After Deleting 17:", nt.in_order_traversal())
