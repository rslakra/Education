#
# Author: Rohtash Lakra
#
from entity.message import Message
from tests._abstract import AbstractTest


class MessageTest(AbstractTest):
    """Unit-tests for message.py"""

    def test_message(self):
        print("test_message")
        wipers = Message("Windshield wipers turned on")
        hazard_lights = Message("Hazard lights turned on")
        print(f"wipers={wipers}, hazard_lights={hazard_lights}")
        self.assertIsNotNone(wipers)
        self.assertIsNotNone(hazard_lights)
        print()


# Starting point
if __name__ == 'main':
    MessageTest().start()
