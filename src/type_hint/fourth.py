# objetivo: se aprofundar no type hinting em classes
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar, final, Self, override


from type_hint.utils import cyan_print, sep_print


class BaseAddress(ABC):
    def __init__(self, street: str, number: int) -> None:
        self.street: str = street
        self.number: int = number

    @abstractmethod
    def get_full_address(self) -> str: ...

    def __repr__(self) -> str:
        attrs_list = [
            f"{k}={v!r}" for k, v in vars(self).items()if not k.startswith("_")
            ]
        attrs_str = ", ".join(attrs_list)   
        class_name = self.__class__.__name__
        return f"{class_name}({attrs_str})"


class NewAddress(BaseAddress):
    @override
    def get_full_address(self) -> str:
        return f"{self.street} {self.number}"


class Address(BaseAddress):
    @override
    def get_full_address(self) -> str:
        return f"{self.street} {self.number}"

@final
class CachedAddress(Address): 
    _cache: ClassVar[dict[str, Self]] = {}
    def __new__(cls, street: str, number: int) -> Self:
        fake_id = f"{street}{number}".lower().replace(" ", "")

        if fake_id in cls._cache:
            cyan_print(f"Address already exists in cache: {fake_id}")
            return cls._cache[fake_id]
        
        instance =  super().__new__(cls)
        cls._cache[fake_id] = instance
        return instance
    
    def __init__(self, street: str, number: int) -> None:
        if not hasattr(self, "_initialized"):
            super().__init__(street, number)
            self._initialized = True
            cyan_print(f"INITIALIZING CachedAddress: {self.street} {self.number}")

    def clone(self) -> Self:
        return self

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

    def get_addresses(self, index: int) -> Address|None:
        return self._addresses.get(index, None)


if __name__ == "__main__":
    p1 = Person("Alice", 30)
    a1 = Address("Main Street", 123)
    c1 = CachedAddress("Second Street", 456)
    c2 = CachedAddress("Second Street", 456)
    p1.add_addresses(a1, c1, c2)

    sep_print()
    cyan_print(p1)
    cyan_print(p1.get_addresses(0))
    cyan_print(p1.get_addresses(1))
    sep_print()
