class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    def __init__(self,capacity):
        assert(capacity >=8),'capacity must be greater than or equal 8'
        
        self.capacity = capacity;
        self.list = [None] * capacity;
    
    def returnList(self):
        return self.list
    def getList(self):
        return len(self.list)
    
    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash<<5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    
t = HashTable(8)

print(t.djb2('hello'))