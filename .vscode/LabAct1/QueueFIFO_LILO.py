#EXAMPLE of queue program

import queue
#example of queue in FILO method
q =queue.Queue()
numbers = [10, 20, 30, 40 , 50]
for number in numbers:
    q.put(number)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
 
#queue in FIFO method ,same program just replace q=queue.Queue into q==queue.LifoQueue

"""
Another example of queue is Priority que
q =queue.PriorityQueue()
q.put((5,"Nightmare"))
q.put((4,"Worse"))
q.put((3,"Your"))
q.put((1,"Hi,"))
q.put((2,"I am"))
while not q.empty():
    print(q.get())





#back up code
q =queue.Queue()
numbers = [10, 20, 30, 40 , 50]
for number in numbers:
    q.put(number)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())




"""

#Example of Stack program
