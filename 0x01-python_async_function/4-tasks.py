#!/usr/bin/env python3
"""asyncio
"""

import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """severl coroutine
    """
    tasks = []
    for i in range(n):
        tasks.append(asyncio.ensure_future(task_wait_random(max_delay)))
    return sorted(await asyncio.gather(*tasks))
