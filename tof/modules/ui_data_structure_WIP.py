"""
WIP
WIP
WIP
"""

from dataclasses import dataclass


@dataclass
class UiDataCoordinatesOnly:
    name: str | None = None
    coordinates: list[str] | None = None

    def __post_init__(self):
        if self.coordinates is None:
            raise Exception(
                "Standalone coordinates data must have a set of coordinates."
            )
        if not self.name:
            raise Exception("Data must have a name.")


@dataclass
class UiDataImage(UiDataCoordinatesOnly):
    file_type: str | None = None
    image_bounds: list[list[str]] | None = None

    def __post_init__(self):
        """
        Overrides parent post init to make coordinates optional. Add additional validation.
        Generates region from from pairs of coordinates provided.
        Uses file name as name if a name is not provided.
        """
        if not self.name:
            raise Exception("Data needs name.")
        for item in self.image_bounds:
            if len(item) < 2:
                raise Exception(
                    "One of the coordinates in image_bounds does not have 2 entries."
                )