#!/usr/bin/env python3
''' file for printing time elapsed  '''

import asyncio
import time 

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    s = time.perf_counter()
    await asyncio.gather(wait_n(n, max_delay))

    return round((time.perf_counter() - s) / n, 2)
