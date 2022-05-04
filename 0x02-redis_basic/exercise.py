#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache Class"""

    def __init__(self):
        """Class constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        The method generate a random key, store the input data in Redis
        using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
