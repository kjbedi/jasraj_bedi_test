import time
import threading
from threading import Timer


class LruCache:
    """
    This is the Lru Cache class.
    """

    def __init__(self, size, expiration_time):
        """
        This is the constructor of the Lru Cache class.
        :param size: The max size of the cache.
        :param expiration_time: The expiration time of cache in seconds.
        :type size: Int
        :type expiration_time: Int
        """
        # Setting max time and expiration time to the cache LRU object.
        self.data = {}
        self.maxSize = size
        self.maxExpirationTimeInSeconds = expiration_time
        thread = threading.Thread(target=self.delete_expired_values)
        thread.start()

    def add(self, key, value):
        """
        This methods adds the key value pair in the cache memory.
        :param key: The key of the data entry in the cache.
        :param value: The value of the data entry in the cache.
        """
        # Check if key already exists.
        key_match = False
        matched_key = None
        for key_dict in self.data.keys():
            if key_dict[1] == key:
                # key found; delete the key value pair and insert it again
                key_match = True
                matched_key = key_dict

        if key_match:
            del self.data[matched_key]

        if len(self.data) < self.maxSize:
            self.data[(time.time(), key)] = value
        else:
            del self.data[self.key_of_least_recently_used_value()]
            self.add(key, value)

    def access(self, key):
        """
        This methods adds the key value pair in the cache memory.
        :param key: The key of the data entry in the cache.
        :param value: The value of the data entry in the cache.
        """
        # Update timestamp of the object if it is accessed
        if self.return_integrated_key_from_key(key) is not None:
            val = self.data[self.return_integrated_key_from_key(key)]
            del self.data[self.return_integrated_key_from_key(key)]
            self.add(key, val)
            return self.return_integrated_key_from_key(key), val
        return None

    def key_of_least_recently_used_value(self):
        """
        Returns the most recently used key.
        """
        # Sorting all the key values and returning the minimum timestamp from the
        keys = list(self.data.keys())
        return sorted(keys)[0]

    def print(self):
        """
        Prints the key, value of the cache.
        """
        for timestamp in self.data:
            print(timestamp, self.data[timestamp])

    def delete_expired_values(self):
        """
        This method deletes the expired values from the cache.
        """
        print("32")
        time_now = time.time()
        keys_to_del = []
        for key in self.data.keys():
            if abs(key[0] - time_now) > self.maxExpirationTimeInSeconds:
                keys_to_del.append(key)
        for key in keys_to_del:
            del self.data[key]
        self.print()
        Timer(5, self.delete_expired_values).start()

    def return_integrated_key_from_key(self, key):
        """
        This function returns the integrated key with timestamp from the key.
        """
        # Searches the key(with timestamp)
        for key_dict in self.data.keys():
            if key_dict[1] == key:
                return key_dict
        return None
