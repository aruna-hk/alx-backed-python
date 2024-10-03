#!/usr/bin/env python3
"""python asyncio
"""

import asyncio
from typing import TypeVar
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> TypeVar('Task'):
    """return task
    """
    return asyncio.create_task(wait_random(max_delay))
