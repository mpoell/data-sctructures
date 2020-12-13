""" 
Max Heap (Speeds up repeated maximum computation algorithms) 
"""


class MaxHeap:
    heap = list()

    def add_node(self, node):
        self.heap.append(node)
        child = len(self.heap) - 1

        # trickle up
        while child > 0:
            parent = (child - 1) // 2
            if self.heap[child] > self.heap[parent]:
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                child = parent
            else:
                return


    def poproot(self):
        root = 0
        last = len(self.heap) - 1

        self.heap[root], self.heap[last] = self.heap[last], self.heap[root]
        self.heap.pop(last)

        parent = root
        last -= 1

        while parent < last:
            try:
                children = [self.heap[2 * parent + 1], self.heap[2 * parent + 2]]
                child = self.heap.index(max(children))
            except IndexError: #Base Case 1: IndexError -> End of heap
                return

            if self.heap[parent] < self.heap[child]:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                parent = child
            else:
                return # Base Case 2: We've reached order, heap property satisfied

    def print_heap(self):
        print(self.heap)


def heapify(ul):
    heap = MaxHeap()
    for node in ul:
        heap.add_node(node)
    return heap


def main():
    my_list = [5,3,7,10,6,12,1,10,16,8,5,4,55,18,17]

    heap = heapify(my_list)
    heap.print_heap()


if __name__ == "__main__":
    main()
