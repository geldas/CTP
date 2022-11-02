import math

class MinPriorityQueue:
    """Creates priority queue that returns the item with the least value.
    
    Uses binary heap data structure."""
    def __init__(self):
        self.q = []
    
    def _heapify(self, i):
        """Sorts the heap from the index i.
        
        Parameters:
        i (int): index of element to be sorted
        
        """
        left = 2*i+1
        right = 2*i+2
        if left <= len(self.q)-1 and self.q[left][0] < self.q[i][0]:
            if right <=len(self.q)-1:
                if self.q[left][0] <= self.q[right][0]:
                    self._swap(i, left)
                    self._heapify(left)
            else:
                self._swap(i, left)
                self._heapify(left)
        if right <=len(self.q)-1 and self.q[right][0]<self.q[i][0]:
            if left <= len(self.q)-1:
                if self.q[right][0] <= self.q[left][0]:
                    self._swap(i, right)
                    self._heapify(right)
            else:
                self._swap(i, right)
                self._heapify(right)

    def _swap(self, source, destination):
        """Swaps two elements in the queue.
        
        Parameters:
        source (int): index of first element to be swapped in the queue
        destination (int): index of second element to be swapped in the queue
        
        """
        if source != destination:
            swapped = self.q[destination]
            self.q[destination] = self.q[source]
            self.q[source]= swapped
    
    def getLength(self):
        """Returns the length of the queue.
        
        Returns:
        len(self.q) (int): lenght of the queue
        
        """
        return len(self.q)

    def _remove(self, i):
        """Removes the element from the queue and sorts it."""
        self._swap(i, len(self.q)-1)
        self.q.pop(-1)
        self._heapify(i)
        #self.sort()
    
    def pop(self):
        """Returns the data with the topmost value (min/max) and _removes it from the queue.
        
        Returns:
        minItem (tuple): returns minimal item's value and data
    
        """
        self._swap(0, len(self.q)-1)
        minItem = self.q[-1]
        self.q.pop(-1)
        self._heapify(0)       
        #self.sort()
        return minItem

    def sort(self):
        """Sorts the data to be ordered in the exact order.
        
        Note that priority queue is not meant to do this as it should only return the data with
        the min/max value.
        
        """
        ordered_q = []
        for _ in range(len(self.q), 0, -1):
            self._swap(0, len(self.q)-1)
            ordered_q.append(self.q[-1])
            self.q.pop(-1)
            self._heapify(0)
        self.q.clear()
        for j in range(len(ordered_q)):
            self.q.append(ordered_q[j])
            #print(self.q[m])
    
    def insert(self, item):
        """Insert the item to the priority queue that will be sorted according to the value.
        
        Parameters:
        item (tuple): (value, data)
            value (int): value according to which the data should be stored in the queue
            ddata (var): stored data in the queue according to value
            
        """
        self.q.append(item)
        i = len(self.q)-1
        while i>=1:
            parent = math.floor((i-1)/2)
            if self.q[i][0] < self.q[parent][0]:
                self.q[i] = self.q[parent]
                self.q[parent] = item
                i = parent
            else:
                break
        #self.sort()

    def printHeap(self):
        """Prints the queue, that uses heap data structure
        
        Note, that heap is not in the exact order, the priority queue is not even meant to return ordered array!
        If you still need to sort the data in exact order, use sort method.
        
        """
        for i in self.q:
            print("%s-%s, " % (i[0], i[1]), end =" ")
        print()

    def update(self, data):
        """Updates the value of specified data if exists in the queue.
        
        Parameters:
        data (tuple): (updated_value, stored_data):
            updated_value (int): updated data's new value
            stored_data (int): the data stored in the queue which value is changed
            
        """
        for i in range(len(self.q)):
            if data[1] == self.q[i][1]:
                self._remove(i)
                self.insert(data)
        #self._remove(data[1])

    # def create(self, data):
    #     self.q.append(data[0])
    #     for m in range(1, len(data)):
    #         i = len(self.q)
    #         self.q.append(data[m])
    #         while i >= 1:
    #             parent = math.floor((i-1)/2)
    #             if self.q[i] < self.q[parent]:
    #                 self.q[i] = self.q[parent]
    #                 self.q[parent] = data[m]
    #                 i = parent
    #             else:
    #                 break
    #     self.sort()

class MaxPriorityQueue(MinPriorityQueue):
    """Creates priority queue that returns the item with the highest value."""
    
    def _heapify(self, i):
        """Sorts the heap from the index i.
        
        Parameters:
        i (int): index of element to be sorted
        
        """
        left = 2*i+1
        right = 2*i+2
        if left <= len(self.q)-1 and self.q[left][0] > self.q[i][0]:
            if right <=len(self.q)-1:
                if self.q[left][0] >= self.q[right][0]:
                    self._swap(i, left)
                    self._heapify(left)
            else:
                self._swap(i, left)
                self._heapify(left)
        if right <=len(self.q)-1 and self.q[right][0] > self.q[i][0]:
            if left <= len(self.q)-1:
                if self.q[right][0] >= self.q[left][0]:
                    self._swap(i, right)
                    self._heapify(right)
            else:
                self._swap(i, right)
                self._heapify(right)
    
    def insert(self, item):
        """Insert the item to the priority queue that will be sorted according to the value.
        
        Parameters:
        item (tuple): (value, data)
            value (int): value according to which the data should be stored in the queue
            ddata (var): stored data in the queue according to value
            
        """
        self.q.append(item)
        i = len(self.q)-1
        while i>=1:
            parent = math.floor((i-1)/2)
            if self.q[i][0] > self.q[parent][0]:
                self.q[i] = self.q[parent]
                self.q[parent] = item
                i = parent
            else:
                break