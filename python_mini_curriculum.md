
# Python 3 Mini‑Curriculum: Learn by Mistakes → Best Practices
*Version:* 2025-09-02  
*Audience:* Absolute beginners  
*How to use:* Read each topic in order. For each, study a **common mistake**, understand the **misconception**, review the **corrected code**, then do the **mini‑exercise**. After that, read **Best Practices** and answer the **Quick Quiz** to reinforce recall.

---

## 0) Setup (5 minutes)
- Install Python 3.12+ from python.org or use an online notebook (e.g., Colab).  
- Run code in a REPL (`python`), a notebook, or a `.py` file via `python your_file.py`.  
- Use a plain‑text editor or IDE (VS Code). Enable “Format on Save” with a PEP 8 formatter (Black).

---

## 1) Basics: Variables, Types, and Loops

### Common mistake
```python
x = input("Enter a number: ")
y = 10
print(x + y)  # TypeError at runtime
```
**Misconception:** *“`input()` gives me a number.”* In Python, `input()` returns a **string**. Adding a string to an integer fails.

**Corrected code**
```python
x = int(input("Enter a number: "))
y = 10
print(x + y)  # works
```

**Plain‑English explanation:** Convert types explicitly. Use `int(...)`, `float(...)`, or `str(...)` when needed.

#### Another common mistake
```python
total = 0
for i in range(1, 5):
    total =+ i  # typo: =+ means total = (+i)
print(total)     # prints 4, not 10
```
**Misconception:** *“`=+` adds to a variable.”* The in‑place addition operator is `+=`, not `=+`.

**Corrected code**
```python
total = 0
for i in range(1, 5):
    total += i
print(total)  # 10
```

**Mini‑exercise (2–3 min):**  
Ask the user for their age (as text), convert to an integer, add 1, and print: “Next year you’ll be X.” Use a `for` loop to print the numbers 1–5 on one line separated by spaces.

### Best Practices
- Prefer **meaningful names**: `count`, `total_price`, `user_age` (PEP 8: lower_snake_case).
- Keep loops small; if you’re just counting or building simple sequences, consider built‑ins like `sum`, `range`, `join`.
- Avoid hidden conversions; be explicit with types.

**Idiomatic snippet**
```python
ages = [19, 22, 27, 30]
avg_age = sum(ages) / len(ages)
print(f"Average age: {avg_age:.1f}")
```

### Quick Quiz
1. What type does `input()` return?  
2. Which operator adds to a variable in place: `=+` or `+=`?  
3. Write one reason to convert types explicitly.

---

## 2) Functions

### Common mistake
```python
def add(a, b):
    print(a + b)

result = add(2, 3)
print(result + 5)  # TypeError: result is None
```
**Misconception:** *“Printing a value inside a function returns it.”* `print()` just displays; functions must **`return`** values.

**Corrected code**
```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result + 5)  # 10
```

**Plain‑English explanation:** Use `return` to hand a value back to the caller.

#### Another common mistake
```python
def greet(name=[]):
    name.append("Guest")
    return name
```
**Misconception:** *“Default list arguments are fresh each call.”* **Mutable defaults** are shared across calls.

**Corrected code**
```python
def greet(name=None):
    if name is None:
        name = []
    name.append("Guest")
    return name
```

**Mini‑exercise (2–3 min):**  
Write a function `square(n)` that returns `n * n`. Use it to print the squares of 1–5 on one line.

### Best Practices
- Functions should **do one thing** and return a value.
- Use **docstrings** to describe purpose, args, returns.
- Avoid **mutable default arguments**; use `None` as the default and initialize inside.
- Keep parameter names descriptive and short.

**Idiomatic snippet**
```python
def area_circle(radius: float) -> float:
    """Return the area of a circle given its radius (in units^2)."""
    from math import pi
    return pi * radius * radius
```

### Quick Quiz
1. What’s the difference between `print` and `return`?  
2. Why are mutable default arguments dangerous?  
3. Write a function header with a docstring that adds two numbers.

---

## 3) Collections: Lists & Dictionaries

### Common mistake
```python
items = ["a", "b", "c"]
for i in items:
    if i == "b":
        items.remove(i)  # Modifying while iterating
```
**Misconception:** *“It’s safe to remove from a list while iterating over it.”* This can **skip** elements or behave unpredictably.

**Corrected code (make a new list)**
```python
items = ["a", "b", "c"]
items = [x for x in items if x != "b"]
```

#### Another common mistake
```python
prices = {"apple": 1.0}
print(prices["banana"])  # KeyError
```
**Misconception:** *“All keys exist.”* Accessing a missing key raises `KeyError`.

**Corrected code**
```python
prices = {"apple": 1.0}
print(prices.get("banana", 0.0))  # 0.0 default
```

**Plain‑English explanation:** Don’t mutate a list while looping over it; build a new list or iterate over a copy. For dict lookups, use `.get()` or check key existence.

**Mini‑exercise (2–3 min):**  
Given `scores = [55, 72, 90, 38, 100]`, make a new list `passing` with scores ≥ 60 and print it. Then make a dictionary mapping each score to `"pass"` or `"fail"`.

### Best Practices
- Use **list comprehensions** and **dict comprehensions** for simple transforms/filters.
- Use `.get()`, `"key" in dict`, or `dict.setdefault` for safe access.
- Prefer **tuples** for fixed collections of items.

**Idiomatic snippets**
```python
names = ["Ana", "Bo", "Chad"]
lengths = {name: len(name) for name in names}

data = [1, 2, 3, 4, 5]
evens = [x for x in data if x % 2 == 0]
```

### Quick Quiz
1. Why is removing items from a list while iterating risky?  
2. What does `dict.get(key, default)` do?  
3. Write a one‑line list comprehension that cubes numbers 1–5.

---

## 4) Error Handling

### Common mistake
```python
try:
    value = int(input("Age: "))
except:
    print("Something went wrong")
```
**Misconception:** *“Catching all exceptions is fine.”* A bare `except` hides bugs and catches unrelated errors.

**Corrected code**
```python
try:
    value = int(input("Age: "))
except ValueError:
    print("Please enter a whole number.")
```

#### Another common mistake
```python
file = open("data.txt")
# ... use file
# forgot to close
```
**Misconception:** *“The OS will close the file for me.”* Relying on GC can leak resources.

**Corrected code**
```python
with open("data.txt") as file:
    text = file.read()
```

**Plain‑English explanation:** Catch **specific** exceptions; always release resources with `with` (context managers).

**Mini‑exercise (2–3 min):**  
Ask for a filename. Try to open and read it; if the file doesn’t exist, print a friendly message without crashing.

### Best Practices
- Catch the **narrowest** exception you can handle; re‑raise or log others.
- Use `with` statements for files, locks, database connections.
- Fail fast; don’t hide errors that you can’t recover from.

**Idiomatic snippet**
```python
from pathlib import Path

def read_text(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"No such file: {path}")
    return p.read_text(encoding="utf-8")
```

### Quick Quiz
1. Why avoid a bare `except`?  
2. What does a `with` block guarantee?  
3. Which exception is raised by `int("abc")`?

---

## 5) OOP (Classes & Objects)

### Common mistake
```python
class Counter:
    count = 0  # class attribute

    def __init__(self):
        self.count = self.count + 1  # intends per-instance count
```
**Misconception:** *“Class and instance attributes are the same.”* Here `count` is a **class** attribute; using it like an instance counter causes confusion.

**Corrected code**
```python
class Counter:
    def __init__(self):
        self.count = 0  # instance attribute

    def increment(self):
        self.count += 1
```

#### Another common mistake
```python
class Box:
    def __init__(self, items=[]):  # mutable default!
        self.items = items
```
**Misconception:** Same as functions—**mutable defaults** are shared.

**Corrected code**
```python
class Box:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []
```

**Plain‑English explanation:** Know the difference between class vs. instance attributes; avoid mutable defaults.

**Mini‑exercise (3–5 min):**  
Create a `BankAccount` class with `deposit`, `withdraw` (no overdraft), and `balance` attribute. Instantiate two accounts to verify they’re independent.

### Best Practices
- Keep classes **small** and focused. If a class only has functions and no state, it might be a module function instead.
- Use `@dataclass` for simple data containers.
- Prefer **composition over inheritance** unless you need a true “is‑a” relationship.

**Idiomatic snippet**
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

p = Point(1.0, 2.5)
```

### Quick Quiz
1. What’s the difference between class and instance attributes?  
2. When is `@dataclass` helpful?  
3. Why favor composition over inheritance?

---

## 6) Modules & Imports

### Common mistake
```python
# file: math_utils.py
def add(a, b):
    return a + b

# file: main.py
from math_utils import *
print(add(2, 3))
```
**Misconception:** *“`from module import *` is fine.”* It pollutes the namespace and can cause name clashes.

**Corrected code**
```python
# main.py
import math_utils

print(math_utils.add(2, 3))
```

#### Another common mistake
```python
# circular imports
# a.py
from b import func_b

def func_a():
    return "A"

# b.py
from a import func_a

def func_b():
    return "B"
```
**Misconception:** *“Modules can freely import each other.”* **Circular imports** break initialization order.

**Corrected approaches**
- Move shared code into a third module both can import.
- Or import inside functions to avoid top‑level cycles.

```python
# common.py
def func_common():
    return "shared"
```

**Plain‑English explanation:** Keep imports **explicit** and avoid circular dependencies by refactoring shared code.

**Mini‑exercise (3–5 min):**  
Create `helpers.py` with a function `shout(msg)` that returns the message uppercased with `!`. Import it in `app.py` and print `shout("hello")`.

### Best Practices
- Prefer **explicit imports**: `import module` or `from module import name`.
- Organize imports: stdlib, third‑party, local; alphabetize within groups.
- Keep module responsibilities clear; avoid cycles.

**Idiomatic snippet**
```python
# app.py
from pathlib import Path
import sys

from .helpers import shout  # if inside a package

def main(argv=None):
    argv = argv or sys.argv[1:]
    print(shout("ready"))

if __name__ == "__main__":
    main()
```

### Quick Quiz
1. Why avoid `from module import *`?  
2. Name one way to fix a circular import.  
3. Write an explicit import that brings in only `sqrt` from `math`.

---

## Capstone Challenge (Optional, 20–30 min)
Build a tiny **To‑Do CLI**:
- `add <task>` adds a task
- `list` shows tasks with indexes
- `done <index>` marks a task complete
- Persist tasks in a JSON file

**Hints:**
- Use `argparse` for CLI.
- Use a list of dicts: `{"title": str, "done": bool}`.
- Use `with open(..., "w")` + `json.dump` to save.

---

## Style & PEP 8 Highlights
- `lower_snake_case` for variables/functions, `CapWords` for classes.
- Max line length ~79–100 chars; use a formatter (Black).
- Use type hints for clarity: `def f(x: int) -> int:`
- Prefer f‑strings for readable formatting.
- Avoid global state; pass values or use objects.

---

## Extra Practice (Short)
- Write a function that returns the **median** of a list of numbers.
- From a dict of product prices, return the **cheapest (name, price)** pair.
- Read a file and count how many lines contain a given substring.

---

## Appendix: Answers (selected)
- **Section 1:** `input()` returns `str`; operator is `+=`; explicit conversion prevents type errors.  
- **Section 2:** `print` displays; `return` hands back a value; mutable defaults persist across calls.  
- **Section 3:** Removing while iterating can skip elements; `dict.get` returns a default when missing.  
- **Section 4:** Bare `except` hides real bugs; `with` ensures proper cleanup; `int("abc")` → `ValueError`.  
- **Section 5:** Class attrs are shared across instances; `@dataclass` removes boilerplate; composition gives flexibility.  
- **Section 6:** `import *` pollutes; fix cycles by extracting shared code or importing inside functions.
