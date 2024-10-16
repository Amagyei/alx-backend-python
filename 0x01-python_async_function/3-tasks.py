#!/usr/bin/env python3
''' Async function to do some stuff
'''

import asyncio

def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates a task that waits for a random delay.'''
    return asyncio.create_task(wait_random(max_delay))
