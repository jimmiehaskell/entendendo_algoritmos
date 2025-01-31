import json
import time
import unittest

from cap1.binary_search import BinarySearch

bs = BinarySearch

with open('itens.json', 'r') as file:
    data = json.load(file)

lista = data['simple_list']
lista_com_10_itens = data['list_with_10_items']
lista_com_100_itens = data['list_with_100_items']
lista_com_1000_itens = data['list_with_1000_items']


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        print(".......... %s" % self._testMethodName)

    # Checking the implementation of iterative binary search


def test_iterative_binary_search_with_lista(self):
    # ARRANGE
    # You can check the index of each item in the items.json file
    item, expected_index = 3, 1

    # ACT
    # Run the method we created and get the index of the item we were looking for
    index = bs.pesquisa_binaria(lista, item)  # => 1

    # ASSERT
    # Compare the resulting index with the expected index
    self.assertEqual(expected_index, index)  # => 1 == 1


def test_recoursive_binary_search_with_lista(self):
    item, expected_index = 3, 1
    # To run recursive search for an item,
    # we need to determine the minimum and maximum indexes of the list
    low, high = 0, len(lista) - 1

    index = bs.pesquisa_binaria_recursiva(lista, low, high, item)

    self.assertEqual(expected_index, index)


def test_search_for_nonexistent_item(self):
    # Specifically set a number that is not in the list
    item, expected_result = 100, None

    # Trying to find an item that doesn't exist
    index = bs.pesquisa_binaria(lista, item)  # => None

    self.assertEqual(expected_result, index)


def test_binary_search_and_linear_search_execution_time(self):
    item, expected_index = 9887, 990

    # Time required to search
    start_time = time.time()
    binary_search_index = bs.pesquisa_binaria(lista_com_1000_itens, item)  # => None
    bs_time = time.time() - start_time

    # list.index(x) return the index in the list of the first item whose value is x.
    # It is an error if there is no such item.
    # Complexity of list.index(x) is O(n)
    start_time = time.time()
    linear_search_index = lista_com_1000_itens.index(item)
    ls_time = time.time() - start_time

    self.assertEqual(expected_index, binary_search_index)
    self.assertEqual(expected_index, linear_search_index)
    self.assertTrue(bs_time < ls_time)

    # print("--- Time required to search item at the ending ---")
    # print("--- Linear Search %f seconds ---" % (ls_time))
    # print("--- Binary Search %f seconds ---" % (bs_time))


def test_execution_time_for_item_at_the_beginning(self):
    item, expected_index = 55, 10

    # Binary search - time required to search
    start_time = time.time()
    binary_search_index = bs.pesquisa_binaria(lista_com_1000_itens, item)  # => None
    bs_time = time.time() - start_time

    # Linear search - time required to search
    start_time = time.time()
    linear_search_index = lista_com_1000_itens.index(item)
    ls_time = time.time() - start_time

    self.assertEqual(expected_index, binary_search_index)
    self.assertEqual(expected_index, linear_search_index)

    # linear search will be faster, since the item we are looking for
    # is at the beginning of the list
    self.assertTrue(bs_time > ls_time)

    # print("--- Time required to search item at the beginning ---")
    # print("--- Linear Search %f seconds ---" % (ls_time))
    # print("--- Binary Search %f seconds ---" % (bs_time))


if __name__ == '__main__':
    unittest.main()
