#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Create and return function that increments the count for that key
    every time the method is called and returns the value returned by
    the original method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper function"""
        self._redis.incr(key, 1)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function."""
    inputs = f'{method.__qualname__}:inputs'
    outputs = f'{method.__qualname__}:outputs'

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper function"""
        self._redis.rpush(inputs, str(args))

        output = method(self, *args, **kwds)
        self._redis.rpush(outputs, output)
        return output
    return wrapper


class Cache:
    """Cache Class"""

    def __init__(self):
        """Class constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        The method generate a random key, store the input data in Redis
        using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
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
            value = 0
        finally:
            return value
