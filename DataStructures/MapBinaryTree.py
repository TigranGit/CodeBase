""" Binary tree implementation needed for HashMap """


class Node:
    def __init__(self, parent, key, value):
        self.key = key
        self.value = value
        self.size = 1
        self.parent = parent
        self.left = None
        self.right = None

    # Update the size by getting left and right branch sizes
    def update(self):
        self.size = (0 if self.left is None else self.left.size) + (
            0 if self.right is None else self.right.size
        )

    # Add a member to the Node
    def insert(self, key, value):
        self.size += 1
        if key < self.key:
            if self.left is None:
                self.left = Node(self, key, value)
                return self.left
            else:
                return self.left.insert(key, value)
        else:
            if self.right is None:
                self.right = Node(self, key, value)
                return self.right
            else:
                return self.right.insert(key, value)

    # Search the Node for a member
    def search(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.search(key)
        else:
            if self.right is None:
                return None
            else:
                return self.right.search(key)

    # Return Node with the smallest key in the subtree
    def minimum(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    # Return the node with the smallest key which is larger than this key
    # None if it is the largest key in the tree
    def successor(self):
        if self.right is not None:
            return self.right.minimum()
        current = self
        while current.parent is not None and current.parent.right is current:
            current = current.parent
        return current.parent

    # Delete the Node
    def delete(self):
        # set the pointer of the parent directly onto the subtree
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            current = self.parent
            while current.key is not None:
                current.update()
                current = current.parent
            return self
        else:
            s = self.successor()
            self.key, s.key = s.key, self.key
            return s.delete()


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.Node = Node
        self.psroot = self.Node(None, None, None)

    # Reset the root's pointer
    def reroot(self):
        self.root = self.psroot.left

    # Insert into the tree
    def insert(self, key, value):
        if self.root is None:
            self.psroot.left = self.Node(self.psroot, key, value)
            self.reroot()
            return self.root
        else:
            return self.root.insert(key, value)

    # Return the node given a key
    # None if it is not in the tree
    def search(self, key):
        if self.root is None:
            return None
        else:
            return self.root.search(key)

    # Delete the node given a key
    def delete(self, key):
        node = self.search(key)
        if not node is None:
            deleted = node.delete()
            self.reroot()
            return deleted
        return None


""" The main HashMap DataStructure """


class HashMap:
    def __init__(self, size):
        self.count = 0
        self.size = size
        self.stack = [BinarySearchTree() for _ in range(size)]

    # Use python hash for hashing
    def hash(self, key):
        return key.__hash__() % self.size

    # Set the value given the key. Add if not found
    def set(self, key, value):
        hashvalue = self.hash(key)
        findNode = self.stack[hashvalue].search(key)
        if findNode is not None:
            findNode.value = value
        else:
            self.stack[hashvalue].insert(key, value)
            self.count += 1
        return True

    # Return the value given the key. None if not found.
    def get(self, key):
        hashvalue = self.hash(key)
        # This defaults None.
        findNode = self.stack[hashvalue].search(key)
        if findNode is not None:
            return findNode.value
        return None

    # Delete the Node given the key if Node was found
    def delete(self, key):
        hashvalue = self.hash(key)
        findNode = self.stack[hashvalue].search(key)
        if findNode is not None:
            retval = self.stack[hashvalue].delete(key)
            self.count -= 1
            return retval.value
        return None

    # Return the percent of tree loading
    def get_load(self):
        if self.count + self.size == 0:
            return 0
        return self.count / float(self.size)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)


if __name__ == "__main__":
    map = HashMap(20)

    keys = [chr(i) for i in range(ord("a"), ord("n"))]
    values = [i for i in range(len(keys))]

    for key, value in zip(keys, values):
        map.set(key, value)
        print("Load:", map.get_load())

    print("b is", map.get("b"))
    print("c is", map["c"])

    map["default"] = -1
    print("default is", map["default"])

    print("trees in map:", map.stack)
