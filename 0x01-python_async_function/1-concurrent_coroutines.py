#!/usr/bin/env python3
"""asyncio
"""

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """severl coroutine
    """
    tasks = []
    for i in range(n):
        tasks.append(asyncio.ensure_future(wait_random(max_delay)))
    return sorted(await asyncio.gather(*tasks))
