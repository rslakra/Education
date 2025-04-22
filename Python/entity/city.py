#
# Author: Rohtash Lakra
#
from typing import NamedTuple


class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    def __str__(self) -> str:
        """Returns string representation of this object."""
        return f"City <name={self.name}, country={self.country}, year={self.year}, latitude={self.latitude}, longitude={self.longitude}>"

    def __repr__(self):
        """Returns string representation of this object."""
        return str(self)

    @classmethod
    def from_dict(cls, attrs: dict):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )
