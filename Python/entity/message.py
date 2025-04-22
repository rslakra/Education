#
# Author: Rohtash Lakra
#
from dataclasses import dataclass


@dataclass
class Message:
    event: str

    def __str__(self) -> str:
        """Returns string representation of this object."""
        return f"Message <event={self.event}>"

    def __repr__(self):
        """Returns string representation of this object."""
        return str(self)
