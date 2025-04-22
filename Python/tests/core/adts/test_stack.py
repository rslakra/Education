#
# Author: Rohtash Lakra
#
from core.adts.stack import Stack
from tests._abstract import AbstractTest


class StackTest(AbstractTest):
    """Unit-tests for Stack"""

    def test_stack_enqueue(self):
        print("test_stack_enqueue")
        stack = Stack()
        stack.enqueue("Java")
        stack.enqueue("Python")
        stack.enqueue("Shell")
        print(f"stack={stack}, size={len(stack)}")
        self.assertIsNotNone(stack)
        self.assertEqual(3, len(stack))
        # print items
        for item in stack:
            print(item)
        print()

    def test_stack_dequeue(self):
        print("test_stack_dequeue")
        stack = Stack()
        stack.enqueue("Java")
        stack.enqueue("Python")
        stack.enqueue("Shell")
        self.assertIsNotNone(stack)
        self.assertEqual(3, len(stack))
        # remove element
        print(stack.dequeue())
        print(f"stack={stack}, size={len(stack)}")
        self.assertIsNotNone(stack)
        self.assertEqual(2, len(stack))

        # remove element
        print(stack.dequeue())
        print(f"stack={stack}, size={len(stack)}")
        self.assertIsNotNone(stack)
        self.assertEqual(1, len(stack))

        # remove element
        print(stack.dequeue())
        print(f"stack={stack}, size={len(stack)}")
        self.assertIsNotNone(stack)
        self.assertEqual(0, len(stack))
        print()

    def test_stack_iterator(self):
        print("test_stack_iterator")
        stack = Stack()
        stack.enqueue("Java")
        stack.enqueue("Python")
        stack.enqueue("Shell")
        print(f"stack={stack}, size={len(stack)}")
        self.assertIsNotNone(stack)
        self.assertEqual(3, len(stack))
        # print items
        for item in stack:
            print(item)
        print()


# Starting point
if __name__ == 'main':
    StackTest().start()
