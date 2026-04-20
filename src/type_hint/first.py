from typing import Final

name: str = "matheus"
x: int = 10
y: float = 3.14
is_valid: bool = True
complex_number: complex = 1 + 2j
data: bytes = b"Hello"

CONST: str = "This is a constant value"

list_of_numbers: list[int | str] = [1, 2, 3, 4, 5, "a"]
tuple_pair: tuple[int, str] = (1, "two")
tuple_many: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7)

set_numbers: set[int] = {1, 2, 3}
frozen_set_numbers: frozenset[int] = frozenset([1, 2, 3])

dictionary: dict[str, str] = {"key1": "value1", "key2": "value2"}
numbers_range: range = range(10)

nothing: None = None
anything: object = "This can be any type"
some_type: type = int

CONTS_PAIR: Final[list[str]] = ["a", "b"]
