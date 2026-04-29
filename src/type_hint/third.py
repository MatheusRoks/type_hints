# objetivo: type hints em classes

from type_hint.utils import blue_print, green_print, sep_print


class Animal:
    def __init__(self, name: str = "Animal") -> None:
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name.capitalize()

    def make_sound(self) -> None:
        blue_print(f"{self.name!r} makes a sound.")


class Dog(Animal):
    def make_sound(self) -> None:
        green_print(f"{self.name!r} says: Woof!")


class Cat(Animal):
    def make_sound(self) -> None:
        blue_print(f"{self.name!r} says: Meow!")


if __name__ == "__main__":
    cat = Cat("cat")
    dog = Dog("dog")
    cat.make_sound()
    dog.make_sound()
    sep_print()
