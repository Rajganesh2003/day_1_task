"""
   LIST is used for stck operations

   append()----push
Adding Elements to the stack
   pop()----pop
removing element from the stack
"""

stack=[] # empty stack

#adding elements to the stack

stack.append(9)
stack.append(7)
stack.append(5)
stack.append(3)

#after inserting elements
print(stack)

#deleting element from the stack

stack.pop()#lifo method  last in first out
#after deleting elements

print(stack)

