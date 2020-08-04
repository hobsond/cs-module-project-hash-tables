class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Bucket:
    def __init__(self):
        self.head = None
    
    def insert(self,key,value):
        if self.head is None:
            self.head = HashTableEntry(key,value)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = HashTableEntry(key,value)
    
    def getValues(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
        
            

class HashTable:
    def __init__(self,capacity):
        assert(capacity >=8),'capacity must be greater than or equal 8'
        
        self.capacity = capacity;
        self.list = [Bucket()] * capacity;
    
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


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity
    
    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # get the hash value
        
        newHash = self.hash_index(key)
        bucket  = self.list[newHash]
        bucket.insert(key,value)
        bucket.getValues()
        
        
        # if the value of that index node is none 
        # add the value to the index head
        # else find the next empty node in that chain and insert the value



    
t = HashTable(8)
t.put('tod','him')