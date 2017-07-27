import multiprocessing
from functools import partial

def square(queue, number):
	result = number*number
	queue.put(result)


# Executing in Windows#

if __name__ == '__main__':

# Alternatively pools can be used to create multiprocessing. Creating a pool of process, here the number is 4
	pool_of_process = multiprocessing.Pool(processes=4)

# Creating a Manager object to manage queue and make it usable by the processes else will have to face \
# RuntimeError: Queue objects should only be shared between processes through inheritance

	m = multiprocessing.Manager()

# creating a Queue to update all the results shared between proceses.

	queue = multiprocessing.Queue()

	queue = m.Queue()	
	
# partial function is created to send an iterable to the map function else map function will raise an error.

	function = partial(square,queue)

# Using the map function with a sample function
	result = pool_of_process.map(function, [x for x in range(2, 1000)], chunksize = 250)
	pool_of_process.close()

# To make main process waiting
	pool_of_process.join()

# Dequeue and get the results.
	while queue.empty() is False:
		print queue.get()
