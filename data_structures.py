from logging import NOTSET
from types import prepare_class
from uuid import uuid4


class LinkedList:
    class Node:
        def __init__(self, data: int, next=None):
            self.id = uuid4()
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item: int):
        node = self.Node(item)
        if not self.head:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def delete(self, item: int):
        current = self.head
        previous = None

        if current and current.data == item:
            self.head = current.next
            print(f"Deleted head: [{current.data}]!")
            current = None
            return

        while current and current.data != item:
            previous = current
            current = current.next

        if not current:
            raise ValueError("Data not found!")

        previous.next = current.next

        print(f"Deleted [{current.data}]!")
        current = None

    def display(self):
        current = self.head

        while current:
            print(f"[{current.data}] -> ", end="")
            current = current.next
        print("None")

    def _get(self):
        list = []
        current = self.head

        while current:
            list.append(current.data)
            current = current.next

        return list


class Stack:
    def __init__(self):
        self.__data = []
        self.top = None

    def push(self, item):
        if item is None:
            return

        self.__data.insert(0, item)
        self.top = item

    def pop(self) -> int:
        popped_item = self.top
        del self.__data[0]
        self.top = self.__data[0] if self.__data else None
        return popped_item

    def display(self):
        for i, v in enumerate(self.__data):
            print(v)

    # Only UT purposes, use 'display' to view Stack
    def _get(self) -> list:
        return self.__data


class Queue:
    # (top/pop) -> [x,x,x,x,x,x,x] <- (bottom/push)

    def __init__(self):
        self.__data = []
        self.top = None
        self.bottom = None

    def pop(self) -> int:
        if not self.top or not self.bottom:
            raise IndexError("Queue already empty!")
        popped_item = self.top
        del self.__data[0]
        try:
            self.top = self.__data[0]
        except IndexError:
            self.top = self.bottom = None
        return popped_item

    def push(self, item):
        if item is None:
            return

        if not self.top:
            self.top = item

        self.__data.append(item)
        self.bottom = item

    def _rotate(self):
        self.push(self.pop())

    def display(self):
        print(self.__data)

    # Only UT purposes, use 'display' to view Stack
    def _get(self):
        return self.__data


class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
        self.traversal = {"depth": [], "breadth": []}

    def add_vertex(self, u: int):
        if u not in self.adj_list.keys():
            self.adj_list[u] = []

    def delete_vertex(self, u: int):
        if u not in self.adj_list.keys():
            raise ValueError("Node not found in Graph!")

        del self.adj_list[u]

        # Delete the edges to 'u'
        for value in self.adj_list.values():
            if u in value:
                value.remove(u)

    def add_edge(self, u: int, v: int):
        if u not in self.adj_list.keys():
            self.add_vertex(u)
        if v not in self.adj_list.keys():
            self.add_vertex(v)

        self.adj_list[u].append(v)

    def delete_edge(self, u: int, v: int):
        if u not in self.adj_list.keys():
            raise ValueError("Node not found in Graph!")
        if v not in self.adj_list[u]:
            raise ValueError("Edge not found in Graph!")

        self.adj_list[u].remove(v)

    def adjacent(self, u: int, v: int) -> bool:
        if u not in self.adj_list.keys():
            return False
        if v not in self.adj_list[u]:
            return False
        return True

    def neighbours(self, u: int) -> list:
        if u not in self.adj_list.keys():
            raise ValueError("Node not found in Graph!")

        return self.adj_list[u]

    def traverse(self, start_vertex: int, type: str):
        if type == "depth":
            storage = Stack()
        elif type == "breadth":
            storage = Queue()
        else:
            raise ValueError("Invalid traversal type!")

        not_visited = [i for i in self.adj_list.keys() if i != start_vertex]
        current_vertex = start_vertex
        self.traversal[type].append(current_vertex)

        while not_visited:
            for v in self.adj_list[current_vertex]:
                storage.push(v)
            current_vertex = storage.pop()
            if current_vertex in not_visited:
                not_visited.remove(current_vertex)
                self.traversal[type].append(current_vertex)


class BinaryTree:
    class Node:
        def __init__(self, data: int) -> None:
            self.data = data
            self.left = None
            self.right = None

    def __init__(self) -> None:
        self.root = None

    def add(self, item, is_node=False):
        child = item if is_node else self.Node(item)
        if not self.root:
            self.root = child
            return

        current = self.root
        while True:
            if child.data < current.data:
                if not current.left:
                    current.left = child
                    break
                else:
                    current = current.left
            elif child.data > current.data:
                if not current.right:
                    current.right = child
                    break
                else:
                    current = current.right

    def delete(self, target):
        current = previous = self.root

        if current.data == target:  # Deleting root
            self.root = current.right  # Arbitrarily deciding to make right as root
            self.add(current.left, is_node=True)

        while current and current.data != target:
            previous = current
            current = current.left if target < current.data else current.right

        if not current:
            raise ValueError("Node not in Tree!")

        previous.right, previous.left = current.right, current.left
        current = None  # Free up space

    def traverse(self, type="depth") -> list:
        storage = Queue() if type == "breadth" else Stack()
        storage.push(self.root)
        visited = []

        while storage.top:
            current = storage.pop()
            visited.append(current.data)
            storage.push(current.right)
            storage.push(current.left)

        return visited
