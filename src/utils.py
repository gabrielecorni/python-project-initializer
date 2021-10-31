from typing import Callable, Iterable


def for_each(
        fn: Callable,
        iterable: Iterable) -> None:
    """
    Apply a function with side effects to all elements of a collection.
    :param fn: the function to be applied
    :param iterable: collection of elements
    :return: None
    """
    for item in iterable:
        fn(item)


def log_start(
        category: str,
        msg: str) -> None:
    click.echo(f"[{category.upper()}] > {msg}...")


def log_end() -> None:
    click.echo()
