#!/usr/bin/env python3
"""python asyncio
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait async
    """
    _wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(_wait_time)
    return _wait_time
