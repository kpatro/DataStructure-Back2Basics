class Node:
    def __init__(self, prev=None, value=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self, value=None):
        self._head = value

    def add_to_start(self, data):
        if self._head is None:  # 20
            self._head = Node(value=data)

        else:  # 30
            new_node = Node(value=data, next=self._head)
            self._head.prev = new_node
            self._head = new_node
        return self._head

    def _print_values(self, p, c, n):
        print("Previous Value :", p)
        print("Current Value :", c)
        print("Next Value : ", n)
        return

    def _get_length(self):
        temp = self._head
        if self._head is None:
            return
        counter = 0
        while temp:
            temp = temp.next
            counter += 1
        return counter

    def add_to_end(self, data):
        if self._head is None:
            self.add_to_start(data=data)
            return
        current = self._head
        while current.next:
            current = current.next
        new_node = Node(prev=current, value=data)
        current.next = new_node
        # new_node.prev = current

    def add_item(self, data, index):
        start = self._head
        if index < 0 or index is None or index > self.length():
            raise Exception("Index out of range")
        if index == 0:
            self.add_to_start(data=data)
        counter = 0
        while start:
            if counter == index - 1:
                new_node = Node(prev=start, value=data, next=start.next)
                start.next = new_node
                return
            start = start.next
            counter += 1

    def print_val(self):
        if self._head is None:
            print("Empty List")
            return
        start = self._head
        ll_str = ""
        while start:
            ll_str += str(start.value) + "-->"
            start = start.next
        print(ll_str)

    def length(self):
        return self._get_length()

    def remove_at_start(self):
        self._head = self._head.next
        self._head.prev = None
        return

    def remove_at_end(self):
        current = self._head
        while current.next:
            temp = current
            current = current.next
        # print(current.value, temp.value)
        current.prev = None
        temp.next = None

    def remove_at(self, indx):
        if indx < 0 or indx is None or indx > self.length():
            raise Exception("Index out of range")
        if indx == 0:
            self.remove_at_start()
        if indx == self._get_length() - 1:
            self.remove_at_end()
        current = self._head
        counter = 0
        while current:
            if counter == indx - 1:
                temp = current.next.next
                current.next = temp
                temp.prev = current

            current = current.next
            counter += 1

    def get_index(self, data):
        if self._head == data:
            return 0
        curr = self._head
        counter = 0
        while curr:
            counter += 1
            if curr.value == data:
                return counter
            curr = curr.next
        return

    def print_prev_next_at(self, indx):
        if indx < 0 or indx is None or indx > self.length():
            raise Exception("Index out of range")
        temp = self._head
        counter = 0
        while temp:
            # print(temp, temp.value, counter, indx)
            if counter == indx:
                break
            counter += 1
            temp = temp.next

        if temp is None:
            print("No matching Values")
        elif temp.next is None:
            self._print_values(p=temp.prev.value, c=temp.value, n=None)
        elif temp.prev is None:
            self._print_values(p=None, c=temp.value, n=temp.next.value)
        else:
            self._print_values(p=temp.prev.value, c=temp.value, n=temp.next.value)


class DeQueue:
    def __init__(self, data=None):
        self.dll = DoubleLinkedList(data)

    def insertFront(self, value):
        self.dll.add_to_start(data=value)

    def insertRear(self, value):
        self.dll.add_item(data=value, index=self.dll.length())

    def deleteFront(self):
        self.dll.remove_at_start()

    def deleteRear(self):
        self.dll.remove_at_end()
        
