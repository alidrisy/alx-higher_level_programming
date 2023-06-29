#!/usr/bin/python3
"""Define a new class Node."""


class Node:

    def __init__(self, data, next_node=None):
        """Initialize node instance.

        Args:
        data: data in node
        next_node = a pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""Define a new class SinglyLinkedList."""


class SinglyLinkedList:

    def __init__(self):
        """Initialize a class data."""
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value, self.__head)
            return
        newNode = Node(value, self.__head)
        self.__head = newNode

    def __str__(self):
        my_list = []
        node = self.__head
        while node is not None:
            my_list.append(node.data)
            node = node.next_node
        my_list.sort()
        x = '\n'.join(str(i) for i in my_list)
        return x
