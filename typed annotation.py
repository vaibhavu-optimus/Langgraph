"""Typed Dictionaries are a way to define a dictionary with specific keys and value types. This is useful for cases where you want to enforce a certain structure for your data."""

from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str

user = User(name="Alice", age=30, email="alice@gmail.com")


"""Union type annotations allow you to specify that a variable can be one of several types. This is useful for cases where a value may be of different types depending on the context."""

from typing import Union

def process_value(value: Union[int, str]) -> None:
    if isinstance(value, int):
        print(f"Processing integer: {value}")
    elif isinstance(value, str):
        print(f"Processing string: {value}")
    else:
        raise ValueError("Unsupported type")

# This is the new syntax for type annotations in Python 3.10 and later
def process_value_new(value: int | str) -> None:
    if isinstance(value, int):
        print(f"Processing integer: {value}")
    elif isinstance(value, str):
        print(f"Processing string: {value}")
    else:
        raise ValueError("Unsupported type")


"""Optional type annotations allow you to specify that a variable can either be of a certain type or None. This is useful for cases where a value may not always be present."""

from typing import Optional

def process_optional_value(value: Optional[int]) -> None:
    if value is None:
        print("Processing None value")
    else:
        print(f"Processing integer: {value}")


"""Any type annotations allow you to specify that a variable can be of any type. This is useful for cases where you want to accept any value without enforcing a specific type."""

from typing import Any

def process_any_value(value: Any) -> None:
    print(f"Processing value of any type: {value}")


"""Lambda type annotations allow you to specify the types of the input and output of a lambda function. This is useful for cases where you want to enforce a certain structure for your lambda functions."""

from typing import Lambda

square: Lambda[[int], int] = lambda x: x * x
square_result = square(5)
print(f"Square of 5 is: {square_result}")

cube = lambda x: x ** 3
cube_result = cube(3)
print(f"Cube of 3 is: {cube_result}")

nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x ** 2, nums))
print(f"Squared numbers: {squared_nums}")