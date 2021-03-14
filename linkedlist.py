class Node:
    def __init__(self, value=None, link=None):
        self.value = value
        self.next = link
        return


class LinkedList:
    def __init__(self):
        """
        Simple Program for Data Structure Linked List
        """
        self._head = None

    def _get_length(self):
        counter = 0
        temp = self._head
        # print(temp, temp.next, temp.value)

        while temp.next:
            counter += 1
            temp = temp.next
        return counter + 1

    def add_to_start(self, data):
        self._head = Node(value=data, link=self._head)
        return

    def add_to_end(self, data):
        start = self._head
        if not start:  # Empty LL
            self.add_to_start(data=data)

        # create Node with new value
        temp = Node(value=data)
        while start.next:
            start = start.next
        start.next = temp
        del temp

    def add_at(self, data, index):
        if index < 0 or index is None or index > self._get_length():
            raise Exception("Empty Index or Invalid Index Value")

        counter = 0
        if index == 0:
            # print("Loop-1")
            self.add_to_start(data=data)
            return
        elif index == self._get_length():
            # print("Loop-2")
            self.add_to_end(data)
        else:
            # print("Loop-3")
            temp = self._head
            while temp:
                if counter == index - 1:
                    node = Node(data, temp.next)
                    temp.next = node
                    break
                temp = temp.next
                counter += 1

    def add_element(self, data):
        self.add_to_end(data=data)

    def remove_at(self, index):
        # print("Length is :", self._get_length())
        if index < 0 or index is None or index > self._get_length():
            print("Empty Index or Invalid Index Value")
            return

        counter = 0
        if index == 0:
            self._head = self._head.next
            return
        elif index == self._get_length():
            print("Loop-5")
            temp = self._head
            while temp:
                if counter == self._get_length() - 2:
                    temp.next = None
                temp = temp.next
                counter += 1
        else:
            temp = self._head
            while temp:
                if counter == index - 1:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                counter += 1

    def remove_element(self, value):
        idx_value = self.index(data=value)
        print("Index Identified :", idx_value)
        self.remove_at(idx_value)

    def is_empty(self):
        return self._head is None

    def print_val(self):
        if self._head is None:
            print("Empty List")
            return
        temp = self._head
        ll_str = ""
        while temp:
            ll_str += str(temp.value) + "-->"
            temp = temp.next
        print(ll_str)

    def length(self):
        return self._get_length()

    def index(self, data):
        idx = 0
        start = self._head
        # print(start, start.value, start.next)
        while start:
            if start.value == data:
                return idx
            start = start.next
            idx += 1
        # print(idx, self.length())
        if idx == self.length():
            return None




# data structure and algorithm
ll_4 = LinkedList()
empty = ll_4.is_empty()
print("Empty : " + str(empty))
ll_4.add_to_start(5)
ll_4.add_to_start(10)
ll_4.add_to_start(15)
ll_4.print_val()
ll_len = ll_4.length()
print("Length of Linked List : ", ll_len)
ll_4.add_to_end(32)
ll_4.add_to_end(54)
ll_4.print_val()
ll_4.add_at(data=20, index=3)
ll_4.add_at(64, 2)
ll_4.add_at(27, 4)
ll_4.print_val()
ll_len = ll_4.length()
print("Length of Linked List : ", ll_len)
idx = ll_4.index(72)
print("Index of Linked List value: ", idx)
ll_4.remove_element(15)
ll_len = ll_4.length()
print("Length of Linked List : ", ll_len)
ll_4.print_val()
