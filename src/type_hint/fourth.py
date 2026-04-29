# objetivo: se aprofundar no type hinting em classes
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import override

from type_hint.utils import cyan_print, sep_print


class BaseAddress(ABC):
    def __init__(self, street: str, number: int) -> None:
        self.street: str = street
        self.number: int = number

    @abstractmethod
    def get_full_address(self) -> str: ...

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}()"


class NewAddress(BaseAddress):
    @override
    def get_full_address(self) -> str:
        return f"{self.street} {self.number}"


class Address(BaseAddress):
    @override
    def get_full_address(self) -> str:
        return f"{self.street} {self.number}"


class CachedAddress(Address): ...


type Addresses = dict[int, Address]


@dataclass
class Person:
    name: str
    age: int
    _addresses: Addresses = field(
        default_factory=dict[int, Address],
        init=False,
        repr=False,
    )
    _new_address_index = 0

    def add_addresses(self, *addresses: Address) -> None:
        for addr in addresses:
            self._addresses[self._new_address_index] = addr
            self._new_address_index += 1

    def get_addresses(self, index: int) -> Address:
        return self._addresses[index]


if __name__ == "__main__":
    p1 = Person("Alice", 30)
    a1 = Address("Main Street", 123)
    p1.add_addresses(a1)

    sep_print()
    cyan_print(p1)
    cyan_print(p1.get_addresses(0))
