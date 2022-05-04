#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Optional, Callable, Any


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

    def get(self, key: str,
            fn: Optional[Callable[..., Any]]) -> Union[str, bytes, int, float]:
        """
        take a key string argument and an optional Callable argument named fn.
        This callable will be used to convert the data back to the
        desired format.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """parametrize Cache.get"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key) -> int:
        """ parametrize Cache.get"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except ValueError:
            value = None
        finally:
            return value
