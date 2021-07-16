"""Driver code."""
import sys
from constants import DEFAULTS
from move_mouse import move


args = []
for idx in range(1, 5):
    try:
        args.append(float(sys.argv[idx]))
    except (IndexError, ValueError):
        args.append(DEFAULTS.get(idx))

move(total_time=args[0], wait_time=args[1], pixels=args[2], duration=args[3])
