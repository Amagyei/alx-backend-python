#!/usr/bin/env python3 
''' first trial of asyncio '''

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    ''' produces a delay between now and max_delay  '''
    delay = random.random() * max_delay  # Generate a random float between 0 and max_delay
    await asyncio.sleep(delay)  # Asynchronously sleep for the generated delay
    return delay 
