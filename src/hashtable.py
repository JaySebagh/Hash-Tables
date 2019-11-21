# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key) # ndex to know where in the hashtable we should add out linkedpair
        pair = LinkedPair(key, value)  # our linkedpair that holds our key value pair

        # check if the node at the index is none
        if self.storage[index] == None:
            # if it's None, insert the linkedpair
            self.storage[index] = pair
            return self.storage[index].value
        else:
            node = self.storage[index]
            while node != None:
                if node.key == key:
                    node.value = value
                    break
                elif node.next == None:
                    node.next = pair
                    break
                node = node.next
            print("pair.kv ", pair.key, pair.value)
            print("index ", index)

        # check if the node at the index is none
          # if it's None, insert the linkedpair
          # if there is something, loop over the node/linkedlist and check if the key already exists
            # if the key exists, just replace it's value
            # if not, add the linkedpair by using self.next --> making the node a linkedlist


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] == None:
            return None
        else:
            node = self.storage[index]
            while node != None:
                if node.key == key:
                    node.key = None
                    node.value = None
                    break
                else:
                    node = node.next
        
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] == None:
            return None
        else:
            node = self.storage[index]
            while node != None:
                if node.key == key:
                    return node.value
                    break
                else:
                    node = node.next


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double size
        self.capacity = self.capacity * 2
        # old storage holds our original storage
        old_storage = self.storage
        # self.storage is now a new storage holding double capacity of None
        self.storage = [None] * self.capacity
        # loop over old storage and each index in the storage
        for i in old_storage:
            while i != None:
                self.insert(i.key, i.value)
                i = i.next

        # iterate storage
            # if at each index it contains more than one node, iterate over that
        # either make copy of old storage
        #iterate through copy and update new storage


        
            




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
