# Variable Annotation
x: int = 1
y: int = 1

# Function Annotation
def add(a: int, b: int) -> int:
    return a + b

# List Annotation
from typing import List
arr: List[List[int]] = [[1, 2], [3, 4]]
print(arr)
arr0: list[list[int]] = [[1, 2], [3, 4]]
print(arr0)

# Dict Annotation
from typing import Dict
x: Dict[str, int] = {'field': 2}
print(x)
x0: dict[str, int] = {'field': '2'}
print(x0)


