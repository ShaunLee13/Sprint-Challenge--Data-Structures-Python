class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [] 
        self.size = 0
        self.tail = -1
        self.head = 0

    def append(self, item):
        #check if storage is full
        if self.size == self.capacity:
            #if true, enqueue item to tail, and decrease the size
            self.enqueue(item)
            self.size -= 1
        else:
            #otherwise, enqueue item    
            self.storage.append(item)
            self.size += 1

    def get(self):
        return self.storage

    def enqueue(self, item):
        #shift tail to next position in loop
        #append item to new tail location
        #increment buffer size
        self.tail = (self.tail + 1) % self.capacity
        self.storage[self.tail] = item
        self.size += 1

