#!/usr/bin/python3
"""async io
"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure asyncio
       time
    """
    _start_time = time.time()
    asyncio.get_event_loop().run_until_complete(wait_n(n, max_delay))
    return (time.time() - _start_time) / n
