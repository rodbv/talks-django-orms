"""Decorators for casas_floripa views."""

import time
import tracemalloc
from functools import wraps


def measure_time_and_memory(view_func):
    """Injects __ELAPSED__ and __MEMORY__ placeholders into response.content."""

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        tracemalloc.start()
        inicio = time.monotonic()

        response = view_func(request, *args, **kwargs)

        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        tempo = f"{time.monotonic() - inicio:.2f}".replace(".", ",")
        memory_str = f"{peak / (1024 * 1024):.1f}"

        response.content = response.content.replace(b"__ELAPSED__", tempo.encode())
        response.content = response.content.replace(b"__MEMORY__", memory_str.encode())

        return response

    return wrapper
