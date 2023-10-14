class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.numbers = 0

    def __repr__(self) -> str:
        nodes = []
        curr = self.head

        while curr is not None:
            if curr is self.head:
                nodes.append(f"[head: {curr.data}]")
            elif curr.next is None:
                nodes.append(f"[tail: {curr.data}]")
            else:
                nodes.append(str(curr.data))
        
            curr = curr.next

        return "->".join(nodes)

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head      
        self.head = new_node
        self.numbers += 1

    def inserting(self,data,index):
        if index==0:
            self.insert(data)
        if index>0:
            new = Node(data)
            position = index
            current = self.head
            while position>1:
                current= current.next
                position -=1
            prev = current
            nextN = current.next
            prev.next = new
            new.next = nextN
    
    def node_at_index(self, index):
        if index >= self.size():
         raise IndexError('Index out of range')
        if index == 0:
            return self.head
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def __getitem__(self, index):
        current = self.head
        for _ in range(index):
            if not current:
                raise IndexError('Linked List index out of range')
            current = current.next
        if not current:
            raise IndexError('Linked List index out of range')
        return current.data

    def slice(self, start, end):
        for i in range(start):
            if not self.head:
                return None
            self.head = self.head.next
        slice_list = LinkedList()
        for i in range(end - start):
            if not self.head:
                break
            slice_list.insert(self.head.data)
            self.head = self.head.next
        return slice_list
    
    def size(self):
        return self.numbers

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data , end=" ")
            current_node = current_node.next
    
    def count(self):
        current = self.head
        count = 0
        while current:
            count+=1
            current = current.next
        return count

    def remove(self,key):
       current = self.head
       previous = None
       found = False
       while current and not found:
           if current.data == key and current is self.head:
               found = True
               self.head = current.next
           elif current.data == key:
               found = True
               previous.next = current.next
           else:
               previous = current
               current = current.next

       return found