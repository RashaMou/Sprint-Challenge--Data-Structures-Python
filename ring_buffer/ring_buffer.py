from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            self.current.value = item
            self.current = self.current.next
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        return list_buffer_contents


buffer = RingBuffer(5)
buffer.append("a")
buffer.append("b")
buffer.append("c")
buffer.append("d")
# print("len", buffer.storage.length)
print("tail", buffer.storage.tail.value)
print(buffer.get())
buffer.append("e")
# print("len", buffer.storage.length)
print("tail", buffer.storage.tail.value)
print(buffer.get())
buffer.append("f")
# print("len", buffer.storage.length)
print("tail", buffer.storage.tail.value)
print(buffer.get())
buffer.append("g")
buffer.append("h")
buffer.append("i")
# print("len", buffer.storage.length)
print("tail", buffer.storage.tail.value)
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
