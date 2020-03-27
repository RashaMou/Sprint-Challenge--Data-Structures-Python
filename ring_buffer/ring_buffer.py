from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            self.storage.add_to_tail(item)
            # replace oldest with newest
            self.current = self.storage.tail
            # set current to next oldest
            self.current.next = self.current
        else:

            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents


buffer = RingBuffer(5)
buffer.append("a")
buffer.append("b")
buffer.append("c")
buffer.append("d")
# print("len", buffer.storage.length)
# print("tail", buffer.storage.tail.value)
print(buffer.get())
buffer.append("e")
# print("len", buffer.storage.length)
# print("tail", buffer.storage.tail.value)
print(buffer.get())
buffer.append("f")
# print("len", buffer.storage.length)
# print("tail", buffer.storage.tail.value)
print(buffer.get())
buffer.append("g")
buffer.append("h")
buffer.append("i")
# print("len", buffer.storage.length)
# print("tail", buffer.storage.tail.value)
print(buffer.get())
# ["f", "g", "h", "i", "e"]


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
