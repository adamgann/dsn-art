"""Map between the spacecraft name and LED pins.
Spacecraft names are as returned by DSN, usually acronyms.
LEDs are pin numbers with 0 closest to Pi and 29 farthest away.
"""


class Mapping:
    """Each class member is a spacecraft name.
    If the spacecraft exists, a list of pins
    is returned."""

    def __init__(self):
        # Fill out dict with each sc's pins.
        self._data = {}
        self._data["lro"] = [0, 1, 2]
        self._data["lucy"] = [3, 4, 5]
        self._data["spp"] = [6, 7, 8]  # Parker
        self._data["mvn"] = [9, 10, 11]  # Maven
        self._data["nhpc"] = [12, 13, 14]  # New Horizons
        self._data["orx"] = [15, 16, 17]  # OSIRIS-REX
        self._data["m20"] = [18, 19, 20]  # Mars 2020
        self._data["jno"] = [21, 22, 23]  # Juno
        self._data["mro"] = [24, 25, 26]
        self._data["psyc"] = [27, 28, 29]  # Psyche

    def __getitem__(self, name):
        if name not in self._data:
            raise ValueError(f"Spacecraft {name} not on board.")
        return self._data[name]

    @property
    def spacecraft(self):
        """Return a list of all spacecraft names."""
        return list(self._data.keys())

