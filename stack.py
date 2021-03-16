class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        """Insert new element as the head of the LinkedList"""
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """Delete the first (head) element in the LinkedList as return it"""
        temp = self.head
        if temp:
            self.head = temp.next
            return temp
        return None

    def reverse(self):
        """Reverse the values present in Linked List"""
        temp = self.head
        previous = [temp]
        while temp:
            temp = temp.next
            previous.append(temp)
        self.head = None
        print(previous)
        for i in previous:
            print(i.value)
            self.append(i)
        return


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        """Push (add) a new element onto the top of the stack"""
        self.ll.insert_first(new_element)

    def pop(self):
        """Pop (remove) the first element off the top of the stack and return it"""
        if self.ll:
            return self.ll.delete_first()

    def is_empty(self):
        return self.ll.head is None

    def reverse(self):
        return self.ll.reverse()
