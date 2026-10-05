# Topic: Data Structures Foundations - Implementing a Stack Using Python Lists
# A Stack follows the Last In, First Out (LIFO) principle.
# Useful for tasks such as undo operations, browser history, and function calls.

stack = []

# Push elements onto the stack
stack.append("Book A")
stack.append("Book B")
stack.append("Book C")

print("Stack after pushes:", stack)

# Pop element from the stack
removed_item = stack.pop()
print("Removed item:", removed_item)

# View the top element
print("Top item:", stack[-1])

print("Current stack:", stack)