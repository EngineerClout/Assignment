class ArrayQueue:
    """
    FIFO (First In, First Out) queue implementation using a Python list as underlying storage.

    This is a CIRCULAR QUEUE - imagine the array as a circle where after the last position,
    we wrap back to the first position. This prevents us from having to shift all elements
    when we remove items from the front.
    """

    # Default capacity for new queues - this is the maximum number of elements
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """
        Create an empty queue.

        We initialize three important things:
        1. _data: A list filled with None values (our "array")
        2. _size: How many actual elements are in the queue (starts at 0)
        3. _front: The index where the first element is located (starts at 0)
        """
        # Create a list with DEFAULT_CAPACITY slots, all filled with None
        # Think of this as creating 10 empty parking spaces in a circular parking lot
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY

        # Keep track of how many cars (elements) are actually parked
        self._size = 0

        # Keep track of where the first car is parked (front of the line)
        self._front = 0

    def __len__(self):
        """
        Return the number of elements currently in the queue.
        This is like counting how many cars are in our circular parking lot.
        """
        return self._size

    def is_empty(self):
        """
        Check if the queue has no elements.
        Returns True if empty, False if it has elements.
        """
        return self._size == 0

    def first(self):
        """
        Return (but don't remove) the element at the front of the queue.
        This is like looking at the first person in line without making them leave.

        Raises Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')

        # The front element is at position self._front in our array
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element of the queue (FIFO - First In, First Out).
        This is like the first person in line leaving and getting served.

        THE KEY CONCEPT: Instead of shifting all elements left (which is slow),
        we just move our _front pointer to the next position and use MODULO
        arithmetic to wrap around when we reach the end of the array.

        Raises Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')

        # Get the element at the front of the queue
        answer = self._data[self._front]

        # Clear the old front position to help with garbage collection
        # (Python will clean up the memory better this way)
        self._data[self._front] = None

        # HERE'S THE MAGIC: Move the front pointer to the next position
        # The % operator makes it "wrap around" - if we're at the last position
        # and add 1, we go back to position 0 (like a circular parking lot)
        self._front = (self._front + 1) % len(self._data)

        # We now have one less element in the queue
        self._size -= 1

        return answer

    def enqueue(self, element):
        """
        Add an element to the rear (back) of the queue.
        This is like a new person joining the back of the line.

        THE KEY CONCEPT: We calculate where the "back" of the queue is
        using modulo arithmetic: (front + size) % capacity
        This automatically wraps around the array when needed.
        """
        # Check if the queue is full
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # Double the capacity

        # Calculate where to put the new element (at the back of the queue)
        # If front=3 and size=4, then back position = (3+4) % 10 = 7
        # If front=8 and size=4, then back position = (8+4) % 10 = 2 (wraps around!)
        back_position = (self._front + self._size) % len(self._data)

        # Place the new element at the calculated back position
        self._data[back_position] = element

        # We now have one more element in the queue
        self._size += 1

    def _resize(self, new_capacity):
        """
        Resize the underlying array to a new capacity.
        This is called when the queue gets full and we need more space.

        IMPORTANT: When we resize, we need to "unwrap" the circular structure
        and create a new linear arrangement starting from index 0.
        """
        # Create a new, bigger array
        old_data = self._data
        self._data = [None] * new_capacity

        # Copy all elements from the old array to the new one,
        # starting from the front and going in queue order
        current_index = self._front
        for i in range(self._size):
            # Copy each element to the new array in order
            self._data[i] = old_data[current_index]
            # Move to the next element, wrapping around if necessary
            current_index = (current_index + 1) % len(old_data)

        # Reset the front to position 0 since we've reorganized everything
        self._front = 0


# Custom exception class for empty queue operations
class Empty(Exception):
    """Exception raised when trying to access elements from an empty queue."""
    pass
class Empty(Exception):
    """Exception raised when trying to access elements from an empty queue."""
    def __init__(self, message="Queue is empty"):
        self.message = message
        super().__init__(self.message)



# Example usage and demonstration
if __name__ == "__main__":
    # Create a new queue
    queue = ArrayQueue()

    print("=== CIRCULAR QUEUE DEMONSTRATION ===")
    print(f"Initial queue size: {len(queue)}")
    print(f"Is queue empty? {queue.is_empty()}")

    # Add some elements (enqueue operations)
    print("\n--- Adding elements to the queue ---")
    elements_to_add = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

    for person in elements_to_add:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    # Show the front element without removing it
    print(f"\nPerson at the front of the line: {queue.first()}")

    # Remove some elements (dequeue operations)
    print("\n--- Serving people from the front of the queue ---")
    for i in range(3):
        served_person = queue.dequeue()
        print(f"Served: {served_person}. Queue size is now: {len(queue)}")

    # Add more elements to show the circular nature
    print("\n--- Adding more people (this will wrap around in the array) ---")
    more_people = ['Frank', 'Grace', 'Henry']

    for person in more_people:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    # Show what's left in the queue
    print(f"\nPerson currently at the front: {queue.first()}")
    print(f"Total people still in queue: {len(queue)}")

    # Demonstrate the wrap-around by showing internal state
    print(f"\nInternal details:")
    print(f"Front index: {queue._front}")
    print(f"Array contents: {queue._data}")
    print("(None values are empty slots in our circular array)")
