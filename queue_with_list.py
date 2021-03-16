class Queue:
    def __init__(self, head=None):
        self.value = [head]

    def enqueue(self, new_element):
        self.value.append(new_element)

    def peek(self):
        return self.value[0]

    def dequeue(self):
        self.value.pop(0)

    def print_all(self):
        print(self.value)
        return
