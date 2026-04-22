from collections.abc import Callable

from type_hint.utils import green_print, red_print, sep_print


def remove_duplicates(items: list[str]) -> list[str]:
    to_dict = dict.fromkeys(items)
    return list(to_dict.keys())


list_of_strings = ["apple", "banana", "apple", "orange", "banana"]
unique_strings = remove_duplicates(list_of_strings)


def with_callback(x: float, y: float, callback: Callable[[str], None]) -> None:
    result = x + y
    callback(f"The result of adding {x} and {y} is: {result}")


if __name__ == "__main__":
    sep_print()
    red_print(f"Original list: {list_of_strings}")
    green_print(f"Unique strings: {unique_strings}")
    sep_print()
    with_callback(3.5, 2.5, green_print)
    sep_print()
