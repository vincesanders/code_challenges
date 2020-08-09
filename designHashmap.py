import math
class Node:
    def __init__(self,key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key=None, value=None):
        if value is None: # validate both key and value entered
            self.head = None
        else:
            self.head = Node(key, value)

    def __str__(self):
        return_string = '['
        if self.head is None:
            return return_string + 'None]'
        current = self.head
        while current.next is not None:
            return_string += f'({current.key}: {current.value}), '
            current = current.next
        return return_string + f'({current.key}: {current.value})' + ']'

    #returns the new head
    def add_to_head(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
        else:
            node = Node(key, value)
            node.next = self.head
            self.head = node
        return self.head

    def find_by_value(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    # returns value
    def find_by_key(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def insert(self, key, value):
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return current
            current = current.next
        # if key is not present in list, add to head
        self.add_to_head(key, value)

    def delete(self, key):
        if self.head is None:
            return None
        current = self.head
        if current.key == key: #the head is to be deleted
            value = current.value
            self.head = current.next
            return value
        while current.next is not None:
            if current.next.key == key:
                #this is what we need to delete
                value = current.next.value
                current.next = current.next.next
                return value
            current = current.next
        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class MyHashMap:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=2069):
        # Your code here
        self.capacity = capacity
        self.storage = []
        self.load = 0
        for _ in range(capacity):
            self.storage.append(HashTableEntry(None, None))

    def __str__(self):
        return_str = '['
        for i in range(self.capacity - 1):
            return_str += f'{self.storage[i]}, '
        return return_str + f'{self.storage[self.capacity - 1]}]'

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.load / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash = 14695981039346656037
        prime = 1099511628211
        size = 2**64
        for c in key:
            hash = (hash * prime) % size
            hash = hash ^ ord(c)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in str(key):
            # <<5 shife bits left by 5 ex: 00000001 => 00100000
            # hash = (( hash << 5) + hash) + ord(c)
            hash = hash * 33 + ord(c)
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
        self.load += 1
        # check load factor
        if self.get_load_factor() > 0.7:
            # if above 0.7, resize to double capacity
            self.resize(self.capacity * 2)
        index = self.hash_index(key)
        self.storage[index].insert(key, value)


    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        self.load -= 1
        # check load factor
        if self.get_load_factor() < 0.2:
            # if below 0.2, resize to half capacity
            self.resize(math.ceil(self.capacity / 2))
        index = self.hash_index(key)
        return self.storage[index].delete(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        return self.storage[index].find_by_key(key)


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # create a new hashtable
        new_hashtable = MyHashMap(new_capacity)
        # add values from old hashtable to new hashtable
        for hte in self.storage:
            # loop through values of hte (linked list)
            current = hte.head
            while current is not None:
                # add each value to new hashtable
                new_hashtable.put(current.key, current.value)
                current = current.next
        # make old hashtable = new hashtable
        self.capacity = new_hashtable.capacity
        self.storage = new_hashtable.storage
        self.load = new_hashtable.load
