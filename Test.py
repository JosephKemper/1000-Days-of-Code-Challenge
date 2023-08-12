from queue import Queue

my_queue = Queue()

# Enqueue
my_queue.put('a')
my_queue.put('b')
my_queue.put('c')

# Dequeue
item = my_queue.get()
print(f"Dequeued item: {item}")

# Find size
size = my_queue.qsize()
print(f"Approximate size of queue: {size}")

# Check if empty
is_empty = my_queue.empty()
print(f"Is queue empty? {is_empty}")