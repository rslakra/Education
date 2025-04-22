#
# Author: Rohtash Lakra
#
import logging

from core.adts.queue import Queue, PriorityQueue
from core.enums import MessagePriority
from tests._abstract import AbstractTest

logger = logging.getLogger(__name__)


class QueueTest(AbstractTest):
    """Unit-tests for Queue"""

    def test_queue_enqueue(self):
        print("test_queue_enqueue")
        queue = Queue()
        queue.enqueue("Python")
        queue.enqueue("Java")
        queue.enqueue("Script")
        queue.enqueue("Shell")

        print()
        print(f"queue={queue}, size={len(queue)}")
        self.assertIsNotNone(queue)
        self.assertEqual(4, len(queue))
        # print items
        for item in queue:
            print(item)
        print()

    def test_queue_dequeue(self):
        print("test_queue_dequeue")
        queue = Queue()
        queue.enqueue("Python")
        queue.enqueue("Java")
        queue.enqueue("Script")
        queue.enqueue("Shell")
        #
        self.assertIsNotNone(queue)
        self.assertEqual(4, len(queue))
        print()

        # remove element
        print(queue.dequeue())
        print(f"queue={queue}, size={len(queue)}")
        self.assertIsNotNone(queue)
        self.assertEqual(3, len(queue))

        # remove element
        print(queue.dequeue())
        print(f"queue={queue}, size={len(queue)}")
        self.assertIsNotNone(queue)
        self.assertEqual(2, len(queue))

        # remove element
        print(queue.dequeue())
        print(f"queue={queue}, size={len(queue)}")
        self.assertIsNotNone(queue)
        self.assertEqual(1, len(queue))

        # remove element
        print(queue.dequeue())
        print(f"queue={queue}, size={len(queue)}")
        self.assertIsNotNone(queue)
        self.assertEqual(0, len(queue))
        print()

    def test_queue_iterator(self):
        print("test_queue_iterator")
        queue = Queue()
        queue.enqueue("Python")
        queue.enqueue("Java")
        queue.enqueue("Script")
        queue.enqueue("Shell")
        self.assertIsNotNone(queue)
        self.assertEqual(4, len(queue))
        # print items
        for item in queue:
            print(item)
        print()

    def test_PriorityQueue(self):
        logger.debug("+test_PriorityQueue()")

        pq = PriorityQueue()
        pq.enqueue(MessagePriority.IMPORTANT, "Windshield wipers turned on")
        pq.enqueue(MessagePriority.NEUTRAL, "Radio station tuned in")
        pq.enqueue(MessagePriority.CRITICAL, "Brake pedal depressed")
        pq.enqueue(MessagePriority.IMPORTANT, "Hazard lights turned on")
        print(f"pq={pq}")
        self.assertIsNotNone(pq)
        # self.assertEqual(4, len(pq))
        print()
        result = pq.dequeue()
        print(f"result={result}")
        # self.assertEqual("('CRITICAL', 'Brake pedal depressed')", str(result))
        self.assertEqual('Brake pedal depressed', result)
        print(pq.dequeue())
        print(pq.dequeue())
        print(pq.dequeue())
        # print items
        # for item in pq:
        #     print(item)

        logger.debug("-test_PriorityQueue()")
        print()


# Starting point
if __name__ == 'main':
    QueueTest().start()
