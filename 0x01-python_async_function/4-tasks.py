#!/usr/bin/env python3
"""asyncio
"""

import asyncio
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """severl coroutine
    """
    tasks = []
    for i in range(n):
        tasks.append(asyncio.ensure_future(task_wait_random(max_delay)))
    return await asyncio.gather(*tasks)
