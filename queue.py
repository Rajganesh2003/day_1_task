"""
   Queue is let consider list
   append is used to add the iteam to the queue
   pop(0) is used to delete the first iteam in the queue

   queue is the first in first out method 
"""


#example

queue=[]#empty queue

#Adding elements to the queue

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

#printing queue elements

print(queue)

#deleting queue element

queue.pop(0)

#after deleting printing queue

print(queue)
