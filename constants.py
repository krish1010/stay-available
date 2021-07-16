"""Constants."""
from enum import Enum


class Parameters(Enum):
    """Parameters to execute move movement."""

    TOTAL_TIME = 1
    INTERMEDIATE_TIME = 2
    PIXELS = 3
    DURATION = 4


DEFAULTS = {
    Parameters.TOTAL_TIME.value: 1,
    Parameters.INTERMEDIATE_TIME.value: 60,
    Parameters.PIXELS.value: 5,
    Parameters.DURATION.value: 1,
}
