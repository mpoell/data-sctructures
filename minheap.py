"""
Min Heap
""" 
  
import sys 
  

class MinHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  

    def parent(self, pos):
        """
        Returns position of parent node for
        node currently at position pos.
        """ 
        return pos//2
  
   
    def left_child(self, pos):
        """
        Returns postition of left child for
        node currently at postition pos.
        """ 
        return 2 * pos 
  
    
    def right_child(self, pos):
        """
        Returns position of right child for
        node currently at postition pos.
        """ 
        return (2 * pos) + 1
  
   
    def is_leaf(self, pos): 
        """
        Returns True if node at position pos
        is a leaf node, else False.
        """
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
  
    
    def swap(self, pos1, pos2): 
        """
        Swaps positions between two nodes in heap.
        """
        self.Heap[pos1], self.Heap[pos2] = self.Heap[pos2], self.Heap[pos1] 
  

    def min_heapify(self, pos):
        """
        Maintain, or restore, heap property with 
        respect to node at position pos.
        """ 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.is_leaf(pos): 
            if (self.Heap[pos] > self.Heap[self.left_child(pos)] or 
               self.Heap[pos] > self.Heap[self.right_child(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.left_child(pos)] < self.Heap[self.right_child(pos)]: 
                    self.swap(pos, self.left_child(pos)) 
                    self.min_heapify(self.left_child(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.right_child(pos)) 
                    self.min_heapify(self.right_child(pos)) 
  

    def insert(self, element): 
        """
        Inserts node into heap. Maintains
        heap property.
        """
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  

    def print_heap(self): 
        """
        Prints contents of heap.
        """
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
     
    def min_heap(self):
        """
        Builds the min heap using min_heapify.
        """ 
  
        for pos in range(self.size//2, 0, -1): 
            self.min_heapify(pos) 
  
    
    def remove(self):
        """
        Returns and removes the minimum
        value element from the heap.
        """ 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.min_heapify(self.FRONT) 
        return popped 
  

# Driver Code 
def main(): 
      
    print('The minHeap is ') 
    minHeap = MinHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    minHeap.min_heap() 
  
    minHeap.print_heap() 
    print("The Min val is " + str(minHeap.remove()))


if __name__ == "__main__":
    main()