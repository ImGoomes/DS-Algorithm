class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert__recursive(data, self.root)

    def _insert__recursive(self, data, node) -> None:
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                return self._insert__recursive(data, node.right)
        else:
            if node.left is None:
                node.left = Node(data)
            else:
                return self._insert__recursive(data, node.left)

    def search(self, data) -> bool:
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data) -> bool:
        if node is None:
            return False

        if data == node.data:
            return True

        if data > node.data:
            return self._search_recursive(node.right, data)

        else:
            return self._search_recursive(node.left, data)


def main():
    tree = BinaryTree()
    tree.insert(9)
    tree.insert(2)
    tree.insert(6)
    tree.insert(5)
    tree.insert(4)
    tree.insert(1)
    tree.insert(3)
    tree.insert(14)

    print(tree.search(10))
    print(tree.search(4))


if __name__ == "__main__":
    main()
