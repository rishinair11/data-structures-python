from unittest import TestCase
from reverse_list import reverse_list
from palindrome import is_palindrome
from subsequence import lcs
from binary_search import search_in_list
from rotate_list import rotate_list
from fibonacci import fetch_nth_fibonacci_number

from data_structures import LinkedList, Stack, Graph, BinaryTree


def create_mock_linked_list(length: int):
    mock_ll = LinkedList()
    for i in range(1, length + 1):
        mock_ll.add(i)
    return mock_ll


def create_mock_stack(length: int):
    mock_stack = Stack()
    for i in range(1, length + 1):
        mock_stack.push(i)
    return mock_stack


def create_mock_graph():
    mock_graph = Graph()

    mock_graph.add_edge(1, 2)
    mock_graph.add_edge(1, 3)
    mock_graph.add_edge(1, 4)
    mock_graph.add_edge(2, 4)
    mock_graph.add_edge(2, 5)
    mock_graph.add_edge(2, 6)
    mock_graph.add_edge(3, 2)
    mock_graph.add_edge(3, 4)
    mock_graph.add_edge(3, 5)

    return mock_graph


class TestReverseList(TestCase):
    def test_returns_reverse_list_odd_length(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(reverse_list(list), [5, 4, 3, 2, 1])

    def test_returns_reverse_list_even_length(self):
        list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(reverse_list(list), [6, 5, 4, 3, 2, 1])


class TestPalindrome(TestCase):
    def test_should_return_true_for_palindrome(self):
        string = "malayalam"
        self.assertTrue(is_palindrome(string))

    def test_should_return_false_for_not_palindrome(self):
        string = "rishikesh"
        self.assertFalse(is_palindrome(string))


class TestLCS(TestCase):
    def test_return_lcs(self):
        string_1 = "apple pie available"
        string_2 = "come have some apple pies"

        self.assertEqual(lcs(string_1, string_2), "apple pie")


class TestBinarySearch(TestCase):
    def test_find_number_in_list_odd_length_success(self):
        numbers = [7, 8, 3, 6, 1, 0, 4, 9, 10]
        target_number = 8
        self.assertTrue(search_in_list(numbers, target_number))

    def test_find_number_in_list_even_length_success(self):
        numbers = [7, 8, 3, 6, 1, 0, 4, 9]
        target_number = 8
        self.assertTrue(search_in_list(numbers, target_number))

    def test_find_number_in_list_odd_length_fail(self):
        numbers = [7, 8, 3, 6, 1, 0, 4, 9, 10]
        target_number = 999
        self.assertFalse(search_in_list(numbers, target_number))

    def test_find_number_in_list_even_length_fail(self):
        numbers = [7, 8, 3, 6, 1, 0, 4, 9]
        target_number = 999
        self.assertFalse(search_in_list(numbers, target_number))


class TestRotateList(TestCase):
    def test_should_return_rotated_list(self):
        list = [1, 2, 3, 4, 5, 6]
        k = 2
        self.assertEqual(rotate_list(list, k), [3, 4, 5, 6, 1, 2])


class TestFibonacciNumbers(TestCase):
    def test_should_return_list_of_fib_numbers(self):
        n = 10
        self.assertEqual(fetch_nth_fibonacci_number(n), 55)


class TestLinkedList(TestCase):
    def test_should_create_empty_linkedlist(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

        # Cleanup
        ll = None

    def test_should_add_node_to_linkedlist(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)

        self.assertEqual(ll._get(), [1, 2])
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.tail.data, 2)
        ll.display()

        # Cleanup
        ll = None

    def test_should_delete_value_from_linkedlist(self):
        value_to_be_deleted = 6
        ll = create_mock_linked_list(10)

        self.assertEqual(ll._get(), [i for i in range(1, 11)])
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.tail.data, 10)

        ll.delete(value_to_be_deleted)

        self.assertEqual(
            ll._get(), [i for i in range(1, 11) if i != value_to_be_deleted]
        )
        ll.display()

        # Cleanup
        ll = None

    def test_should_raise_error_if_deleting_unknown_value(self):
        value_to_be_deleted = 24
        ll = create_mock_linked_list(10)

        self.assertEqual(ll._get(), [i for i in range(1, 11)])
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.tail.data, 10)
        self.assertRaises(ValueError, ll.delete, value_to_be_deleted)

        ll.display()

        # Cleanup
        ll = None

    def test_should_set_new_head_when_deleting_head(self):
        ll = create_mock_linked_list(5)

        self.assertEqual(ll.head.data, 1)
        ll.delete(1)
        self.assertEqual(ll.head.data, 2)

        # Cleanup
        ll = None


class TestStack(TestCase):
    def test_should_create_empty_stack(self):
        s = Stack()
        self.assertIsNone(s.top)
        self.assertEqual(s._get(), [])

        # Cleanup
        s = None

    def test_should_populate_stack(self):
        s = create_mock_stack(3)

        self.assertEqual(s.top, 3)
        self.assertEqual(s._get(), [3, 2, 1])

        # Cleanup
        s = None

    def test_should_pop_elements(self):
        s = create_mock_stack(6)

        self.assertEqual(s.top, 6)

        self.assertEqual(s.pop(), 6)
        self.assertEqual(s.top, 5)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.top, 4)

        self.assertEqual(s._get(), [4, 3, 2, 1])

        # Cleanup
        s = None


class TestGraph(TestCase):
    def test_should_add_nodes_to_graph(self):
        g = create_mock_graph()
        self.assertEqual(
            g.adj_list, {1: [2, 3, 4], 2: [4, 5, 6], 3: [2, 4, 5], 4: [], 5: [], 6: []}
        )

        # Cleanup
        g = None

    def test_should_create_edge(self):
        g = Graph()
        g.add_edge(1, 2)

        self.assertEqual(g.adj_list, {1: [2], 2: []})

        # Cleanup
        g = None

    def test_should_traverse_graph_depth_first(self):
        g = create_mock_graph()
        g.traverse(1, type="depth")

        self.assertEqual(g.traversal["depth"], [1, 4, 3, 5, 2, 6])

        # Cleanup
        g = None

    def test_should_traverse_graph_breadth_first(self):
        g = create_mock_graph()
        g.traverse(1, type="breadth")

        self.assertEqual(g.traversal["breadth"], [1, 2, 3, 4, 5, 6])

        # Cleanup
        g = None


class TestBinaryTree(TestCase):
    def test_should_create_root_node(self):
        t = BinaryTree()
        t.add(5)

        self.assertEqual(t.root.data, 5)

        t = None

    def test_should_traverse_depth_first(self):
        t = BinaryTree()
        list = [5, 3, 4, 6, 2, 7, 9, 1, 10]
        for item in list:
            t.add(item)
        self.assertEqual(t.traverse("depth"), [5, 3, 2, 1, 4, 6, 7, 9, 10])
        t = None

    def test_should_traverse_breadth_first(self):
        t = BinaryTree()
        list = [5, 3, 4, 6, 2, 7, 9, 1, 10]
        for item in list:
            t.add(item)
        self.assertEqual(t.traverse("breadth"), [5, 6, 3, 7, 4, 2, 9, 1, 10])
        t = None

    def test_should_delete_node_from_tree(self):
        t = BinaryTree()
        list = [6, 4, 8, 3, 5, 7, 9, 1]
        for item in list:
            t.add(item)
        self.assertEqual(t.traverse("depth"), [6, 4, 3, 1, 5, 8, 7, 9])
        t.delete(6)
        self.assertEqual(t.traverse("depth"), [8, 7, 4, 3, 1, 5, 9])
        t = None
