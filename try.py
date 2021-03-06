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
        
        x = HashTableEntry(key,value)
       
        if self.head is None:
            self.head = x 
        else:
            curr = self.head
            
            while curr.next is not None:
                if curr.key is key:
                    curr.value = value
                    return
                curr = curr.next
            curr.next = x
            
            
    
    def getKey(self,key):
        curr= self.head
        
        while curr is not None:
            if curr.key == key:
                return True
            curr= curr.next
        return False
    
    def delete(self,key):
        curr = self.head
        if curr.key == key:
            self.head = curr.next
            self.getValues()
            return
        while curr.key is not key and curr.next is not None:
            if curr.next.key is key:
                
                searchKey = curr.next
                nextKey = searchKey.next 
                curr.next = nextKey
                self.getValues()
                return "deleted"
            else:
                curr=curr.next
        return "could not Find"
        
    def getValues(self):
        curr = self.head
        while curr is not None:
            print(curr.key)
            curr = curr.next
        
            
    def getKeyandValues(self):
        curr = self.head
        x= []
        while curr is not None:
            x.append([curr.key,curr.value])
            curr = curr.next
        return x
        
            

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

    def get(self,key):
        t = self.hash_index(key)
        bucket = self.list[t]
        return bucket.getKey(key)
    
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        
        return self.djb2(key) % self.capacity
    
    def getBucket(self,key):
        x = self.hash_index(key)
        bucket= self.list[x]
        bucket.getValues()
        
    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # get the hash value
        
        newHash = self.hash_index(key)
        hash_entry = self.list[newHash]
        
        
        if self.list[newHash] is not None:
            bucket  = self.list[newHash]
            bucket.insert(key,value)
        else:
            
            self.list[newHash] = Bucket()
            x = self.list[newHash]
            
        
            # x.insert(key,value)
            
        # if self.get_load_factor() > .07:
        #     self.resize(self.capacity * 2)  
            
        # elif self.get_load_factor() <= .02:
        #     self.resize(self.capacity/2)
        
            
        
            
            
        
        
        
        
        # if the value of that index node is none 
        # add the value to the index head
        # else find the next empty node in that chain and insert the value

    def delete(self,key):
        t= self.hash_index(key)
        bucket = self.list[t]
        bucket.delete(key)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        y = [i for i in self.list if i is not None]
        
        numberOfOn = len(y)
        x = self.capacity
        # print(y)
        return numberOfOn / x
    
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        x= []
        for i in self.list:
            if i is not None:
                x += i.getKeyandValues()
        
        self.capacity = new_capacity
        self.list = [None] * self.capacity
        for i in x:
            self.put(i[0],i[1])
        

t = HashTable(8)
t.put('tod','phillip')
t.put('tod','spacechime')
t.put('dot','chimp')
         
    
# x= []
# for i in t.list:
#     if i is not None:
#         x += i.getKeyandValues()
# print(x)


print(t.get('dot'))
print(t.get('tod'))