import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)

logger = logging.getLogger(__name__)

# Topic: Data Structures Foundations - Implementing a Stack Using Python Lists
# A Stack follows the Last In, First Out (LIFO) principle.

stack = []

# Push elements onto the stack
stack.append("Book A")
stack.append("Book B")
stack.append("Book C")

logger.info(f"Stack after pushes: {stack}")

# Pop element from the stack
removed_item = stack.pop()
logger.info(f"Removed item: {removed_item}")

# View the top element
logger.info(f"Top item: {stack[-1]}")

logger.info(f"Current stack: {stack}")