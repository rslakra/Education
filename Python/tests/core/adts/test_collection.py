#
# Author: Rohtash Lakra
#

from tests._abstract import AbstractTest


class CollectionTest(AbstractTest):
    """Unit-tests for Collection"""

    def test_list(self):
        print("test_list")
        instance = list()
        instance.append("Python")
        instance.append("Java")
        instance.append("Script")
        instance.append("Shell")

        print()
        print(f"instance={instance}, size={len(instance)}")
        self.assertIsNotNone(instance)
        self.assertEqual(4, len(instance))
        for item in instance:
            print(f"item={item} at index={instance.index(item)}")
        print()
        # print items
        for index, item in enumerate(instance):
            print(f"index={index}, item={item}")
        print()

    def test_set(self):
        print("test_set")
        instance = set()
        instance.add("Python")
        instance.add("Java")
        instance.add("Script")

        print()
        print(f"instance={instance}, size={len(instance)}")
        self.assertIsNotNone(instance)
        self.assertEqual(3, len(instance))
        for item in instance:
            print(f"item={item}")
        # print items
        for index, item in enumerate(instance):
            print(f"index={index}, item={item}")
        print()

    # def test_List(self):
    #     print("test_List")
    #     instance = List()
    #     instance.append("Python")
    #     instance.append("Java")
    #     instance.append("Script")
    #     instance.append("Shell")
    #
    #     print()
    #     print(f"instance={instance}, size={len(instance)}")
    #     self.assertIsNotNone(instance)
    #     self.assertEqual(4, len(instance))
    #     # print items
    #     for item in instance:
    #         print(item)
    #     print()

    # def test_Deque(self):
    #     print("test_Deque")
    #     instance = Deque()
    #     instance.append("Python")
    #     instance.append("Java")
    #     instance.append("Script")
    #     instance.append("Shell")
    #
    #     print()
    #     print(f"instance={instance}, size={len(instance)}")
    #     self.assertIsNotNone(instance)
    #     self.assertEqual(4, len(instance))
    #     # print items
    #     for item in instance:
    #         print(item)
    #     print()


# Starting point
if __name__ == 'main':
    CollectionTest().start()
