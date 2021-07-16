"""Move mouse."""
import time
import mouse


def move(total_time: float = 1, wait_time: float = 60, pixels: float = 5, duration: float = 1) -> None:
    """Move the mouse.

    Parameters
    ----------
        total_time: float
            Total time the function will run in hours.
        wait_time: float
            Time to wait between completion check in seconds.
        pixels: float
            Pixels to move the mouse.
        duration: float
            Duration to animate the mouse movement.
    """
    end_time = time.perf_counter() + total_time * 60 * 60
    while time.perf_counter() <= end_time:
        time.sleep(wait_time)
        mouse.move(pixels, pixels, absolute=False, duration=duration)
        mouse.click()
        time.sleep(1)
        mouse.move(-pixels, -pixels, absolute=False, duration=duration)
