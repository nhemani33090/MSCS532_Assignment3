class ChainedHashTable:
    """
    Hash Table implementation using chaining to resolve collisions.
    """

    def __init__(self, initial_size=15):
        """
        Initialize the hash table with a specified initial size.
        """
        self.bucket_count = initial_size
        self.entry_count = 0
        self.buckets = [[] for _ in range(self.bucket_count)]  # Create empty chains

    def compute_index(self, key):
        """
        Compute the index for a given key using a hash function.
        The index is calculated as the hash of the key modulo the bucket count.
        """
        return hash(key) % self.bucket_count

    def add(self, key, value):
        """
        Add a key-value pair to the hash table.
        If the key exists, update the value.
        """
        bucket_index = self.compute_index(key)
        chain = self.buckets[bucket_index]

        # Update the value if the key already exists
        for entry in chain:
            if entry[0] == key:
                entry[1] = value
                return

        # Add the key-value pair if the key is not found
        chain.append([key, value])
        self.entry_count += 1

        # Resize if the load factor exceeds the threshold
        if self.calculate_load_factor() > 0.75:
            self.expand_table()

    def retrieve(self, key):
        """
        Retrieve the value associated with the given key.
        Return None if the key is not found.
        """
        bucket_index = self.compute_index(key)
        chain = self.buckets[bucket_index]

        for entry in chain:
            if entry[0] == key:
                return entry[1]

        return None

    def remove(self, key):
        """
        Remove the key-value pair associated with the given key.
        Return True if the removal is successful, or False if the key is not found.
        """
        bucket_index = self.compute_index(key)
        chain = self.buckets[bucket_index]

        for entry in chain:
            if entry[0] == key:
                chain.remove(entry)
                self.entry_count -= 1
                return True

        return False

    def calculate_load_factor(self):
        """
        Calculate the load factor of the hash table.
        """
        return self.entry_count / self.bucket_count

    def expand_table(self):
        """
        Double the number of buckets and rehash all elements into the new table.
        """
        old_buckets = self.buckets
        self.bucket_count *= 2
        self.buckets = [[] for _ in range(self.bucket_count)]
        self.entry_count = 0

        for chain in old_buckets:
            for key, value in chain:
                self.add(key, value)

    def show_table(self):
        """
        Display the current contents of the hash table.
        """
        for index, chain in enumerate(self.buckets):
            print(f"Bucket {index}: {chain}")


# Example Usage
hash_table = ChainedHashTable()

# Adding entries
hash_table.add("John", 45)
hash_table.add("Doe", 32)
hash_table.add("Anna", 67)
hash_table.add("John", 50)  # Update value for "John"

# Retrieving values
print("Retrieve John:", hash_table.retrieve("John"))  # Output: 50
print("Retrieve Doe:", hash_table.retrieve("Doe"))    # Output: 32
print("Retrieve Mark:", hash_table.retrieve("Mark"))  # Output: None

# Removing entries
print("Remove Doe:", hash_table.remove("Doe"))        # Output: True
print("Remove Mark:", hash_table.remove("Mark"))      # Output: False

# Display hash table
hash_table.show_table()
