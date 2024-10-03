#!/usr/bin/python3
"""asyncio
"""

import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    """severl coroutine
    """
    tasks = []
    for i in range(n):
        tasks.append(asyncio.ensure_future(wait_random(max_delay)))
    return await asyncio.gather(*tasks)
