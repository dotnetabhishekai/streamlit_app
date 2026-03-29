"""
Learn Python — Streamlit Web App
==================================
Interactive Python tutorial with 20 lessons, live code editor, and quizzes.
Deploy free on Streamlit Cloud.

Run locally:  streamlit run learn_python_web.py
"""

import streamlit as st
import io
import sys
import traceback

st.set_page_config(page_title="Learn Python", page_icon="🐍", layout="wide")

# ---------------------------------------------------------------------------
# Lessons (same content as the Tkinter version)
# ---------------------------------------------------------------------------
LESSONS = [
    {
        "title": "1. Hello World",
        "topic": "Your First Program",
        "theory": """Every programmer starts here. The `print()` function outputs text to the screen.

```python
print("your message")
```

**Key points:**
- Strings go inside quotes (single `'` or double `"`)
- `print()` can take multiple arguments separated by commas
- You can print numbers without quotes""",
        "example": 'print("Hello, World!")\nprint("My name is", "Python")\nprint(2 + 3)',
        "exercise": "Print your name and your age on two separate lines.",
        "hint": 'print("Alice")\nprint(25)',
        "quiz_q": "What does `print(3 + 4)` output?",
        "quiz_opts": ['"3 + 4"', "7", "34", "Error"],
        "quiz_ans": 1,
        "quiz_exp": "Python evaluates 3 + 4 = 7 first, then print() displays 7.",
    },
    {
        "title": "2. Variables",
        "topic": "Storing Data",
        "theory": """Variables store values so you can use them later.

```python
variable_name = value
```

**Rules:** Letters, numbers, underscores. Can't start with a number. Case-sensitive.

**Common types:**
- `int` — whole numbers: `42`
- `float` — decimals: `3.14`
- `str` — text: `"hello"`
- `bool` — `True` or `False`""",
        "example": 'name = "Alice"\nage = 25\nheight = 5.6\nis_student = True\n\nprint(name, "is", age, "years old")\nprint(type(age))',
        "exercise": "Create variables for a pet's name, age, and breed. Print them in a sentence.",
        "hint": 'pet_name = "Buddy"\npet_age = 3\nbreed = "Golden Retriever"\nprint(pet_name, "is a", pet_age, "year old", breed)',
        "quiz_q": "Which is a valid variable name?",
        "quiz_opts": ["2name", "my-var", "user_age", "class"],
        "quiz_ans": 2,
        "quiz_exp": "user_age is valid. 2name starts with a number, my-var has a hyphen, class is a reserved keyword.",
    },
    {
        "title": "3. Strings",
        "topic": "Working with Text",
        "theory": """Strings are sequences of characters in quotes.

**Operations:**
- Concatenation: `"hello" + " world"`
- Repetition: `"ha" * 3` → `"hahaha"`
- Length: `len("hello")` → `5`
- Indexing: `"hello"[0]` → `"h"`
- Slicing: `"hello"[1:4]` → `"ell"`

**f-strings:**
```python
name = "Alice"
print(f"Hello, {name}!")
```""",
        "example": 'greeting = "Hello"\nname = "World"\nprint(f"{greeting}, {name}!")\nprint("python".upper())\nprint("  spaces  ".strip())\nprint("hello world".split())',
        "exercise": "Create a variable with your full name. Print it in uppercase, its length, and the first 3 characters.",
        "hint": 'full_name = "Alice Smith"\nprint(full_name.upper())\nprint(len(full_name))\nprint(full_name[:3])',
        "quiz_q": 'What does `"python"[1:4]` return?',
        "quiz_opts": ['"pyt"', '"yth"', '"ytho"', '"pyth"'],
        "quiz_ans": 1,
        "quiz_exp": "Slicing [1:4] starts at index 1 ('y') up to (not including) index 4 → 'yth'.",
    },
    {
        "title": "4. Numbers & Math",
        "topic": "Arithmetic Operations",
        "theory": """**Operators:**
| Op | Name | Example |
|---|---|---|
| `+` | Addition | `10 + 3` → `13` |
| `-` | Subtraction | `10 - 3` → `7` |
| `*` | Multiplication | `10 * 3` → `30` |
| `/` | Division | `10 / 3` → `3.33` |
| `//` | Floor division | `10 // 3` → `3` |
| `%` | Modulo | `10 % 3` → `1` |
| `**` | Power | `2 ** 3` → `8` |

Order: PEMDAS (Parentheses → Exponents → Multiply/Divide → Add/Subtract)""",
        "example": "print(10 + 3)\nprint(10 / 3)\nprint(10 // 3)\nprint(10 % 3)\nprint(2 ** 10)\nprint(2 + 3 * 4)\nprint((2 + 3) * 4)",
        "exercise": "Calculate the area of a circle with radius 7 (area = π × r²). Use 3.14159 for π.",
        "hint": 'radius = 7\npi = 3.14159\narea = pi * radius ** 2\nprint(f"Area = {area:.2f}")',
        "quiz_q": "What is `17 % 5`?",
        "quiz_opts": ["3", "2", "3.4", "12"],
        "quiz_ans": 1,
        "quiz_exp": "% is modulo (remainder). 17 ÷ 5 = 3 remainder 2.",
    },
    {
        "title": "5. Lists",
        "topic": "Ordered Collections",
        "theory": """Lists store multiple items in order. They are **mutable**.

```python
fruits = ["apple", "banana", "cherry"]
```

**Common operations:**
- `fruits[0]` → first item
- `fruits[-1]` → last item
- `fruits.append(x)` → add to end
- `fruits.remove(x)` → remove first match
- `fruits.sort()` → sort in place
- `x in fruits` → check membership
- `[x**2 for x in range(5)]` → list comprehension""",
        "example": 'fruits = ["apple", "banana", "cherry"]\nprint(fruits[0])\nfruits.append("date")\nfruits[1] = "blueberry"\nprint(fruits)\n\nfor fruit in fruits:\n    print(f"I like {fruit}")\n\nsquares = [x**2 for x in range(5)]\nprint(squares)',
        "exercise": "Create a list of 5 numbers. Print the sum, the largest, the smallest, and the list sorted in reverse.",
        "hint": 'nums = [42, 8, 15, 23, 4]\nprint(sum(nums))\nprint(max(nums))\nprint(min(nums))\nprint(sorted(nums, reverse=True))',
        "quiz_q": "What does `[1, 2, 3] + [4, 5]` produce?",
        "quiz_opts": ["[1, 2, 3, 4, 5]", "[5, 7, 3]", "Error", "[[1,2,3],[4,5]]"],
        "quiz_ans": 0,
        "quiz_exp": "The + operator concatenates lists → [1, 2, 3, 4, 5].",
    },
    {
        "title": "6. Conditionals",
        "topic": "Making Decisions",
        "theory": """`if/elif/else` lets your code make decisions.

```python
if condition:
    do something
elif other_condition:
    do something else
else:
    default action
```

**Comparison:** `==`, `!=`, `>`, `<`, `>=`, `<=`
**Logical:** `and`, `or`, `not`""",
        "example": 'age = 15\nif age >= 18:\n    print("Adult")\nelif age >= 13:\n    print("Teenager")\nelse:\n    print("Child")\n\nstatus = "even" if 10 % 2 == 0 else "odd"\nprint(status)',
        "exercise": "Check a score (0-100) and print the grade: A (90+), B (80+), C (70+), D (60+), F (below 60).",
        "hint": 'score = 85\nif score >= 90: print("A")\nelif score >= 80: print("B")\nelif score >= 70: print("C")\nelif score >= 60: print("D")\nelse: print("F")',
        "quiz_q": "What prints: `if 0: print('yes') else: print('no')`",
        "quiz_opts": ["yes", "no", "Error", "0"],
        "quiz_ans": 1,
        "quiz_exp": "0 is falsy in Python, so the else branch runs.",
    },
    {
        "title": "7. Loops",
        "topic": "Repeating Actions",
        "theory": """**for loop** — iterate over a sequence:
```python
for item in sequence:
    do something
```

**while loop** — repeat while True:
```python
while condition:
    do something
```

**Control:** `break` (exit loop), `continue` (skip iteration)

**range():** `range(5)` → 0,1,2,3,4 | `range(2,8)` → 2,3,4,5,6,7""",
        "example": 'for i in range(5):\n    print(f"Count: {i}")\n\nn = 1\nwhile n <= 5:\n    print(n, end=" ")\n    n += 1\nprint()\n\ncolors = ["red", "green", "blue"]\nfor i, color in enumerate(colors):\n    print(f"{i}: {color}")',
        "exercise": "Print the multiplication table for 7 (7×1 through 7×10).",
        "hint": 'for i in range(1, 11):\n    print(f"7 x {i} = {7 * i}")',
        "quiz_q": "How many times does `for i in range(3, 8)` run?",
        "quiz_opts": ["3", "5", "6", "8"],
        "quiz_ans": 1,
        "quiz_exp": "range(3, 8) produces 3,4,5,6,7 — 5 numbers.",
    },
    {
        "title": "8. Functions",
        "topic": "Reusable Code Blocks",
        "theory": """```python
def function_name(parameters):
    \"\"\"Docstring\"\"\"
    code
    return value
```

**Key concepts:**
- Parameters — inputs
- Return — sends value back
- Default values: `def greet(name="World")`
- `*args` — variable positional args
- `**kwargs` — variable keyword args""",
        "example": 'def greet(name, greeting="Hello"):\n    return f"{greeting}, {name}!"\n\nprint(greet("Alice"))\nprint(greet("Bob", "Hi"))\n\ndef min_max(numbers):\n    return min(numbers), max(numbers)\n\nlo, hi = min_max([3, 1, 4, 1, 5])\nprint(f"Min: {lo}, Max: {hi}")',
        "exercise": "Write a function that converts Celsius to Fahrenheit (F = C × 9/5 + 32). Test with 0, 100, 37.",
        "hint": 'def celsius_to_fahrenheit(c):\n    return c * 9/5 + 32\n\nprint(celsius_to_fahrenheit(0))\nprint(celsius_to_fahrenheit(100))\nprint(celsius_to_fahrenheit(37))',
        "quiz_q": "What does a function return if there's no return statement?",
        "quiz_opts": ["0", '""', "None", "Error"],
        "quiz_ans": 2,
        "quiz_exp": "Functions without return implicitly return None.",
    },
    {
        "title": "9. Dictionaries",
        "topic": "Key-Value Pairs",
        "theory": """```python
person = {"name": "Alice", "age": 25}
```

**Access:** `person["name"]` or `person.get("email", "N/A")`
**Modify:** `person["age"] = 26` | `del person["age"]`
**Iterate:** `for key, value in person.items():`""",
        "example": 'student = {"name": "Alice", "age": 20, "grades": [90, 85, 92]}\nprint(student["name"])\nprint(student.get("email", "Not set"))\n\nstudent["email"] = "alice@school.edu"\nfor key, value in student.items():\n    print(f"{key}: {value}")\n\nsquares = {x: x**2 for x in range(6)}\nprint(squares)',
        "exercise": "Create a dict for a book (title, author, year, pages). Print each field and check if 'isbn' exists.",
        "hint": 'book = {"title": "Python 101", "author": "Smith", "year": 2024, "pages": 350}\nfor k, v in book.items():\n    print(f"{k}: {v}")\nprint("isbn" in book)',
        "quiz_q": 'What happens with `d = {"a": 1}; print(d["b"])`?',
        "quiz_opts": ["None", "0", "KeyError", '""'],
        "quiz_ans": 2,
        "quiz_exp": "Accessing a missing key with [] raises KeyError. Use .get() for safe access.",
    },
    {
        "title": "10. File Handling",
        "topic": "Reading and Writing Files",
        "theory": """```python
with open("file.txt", "r") as f:
    content = f.read()
```

**Modes:** `"r"` read, `"w"` write, `"a"` append

The `with` block auto-closes the file.

**Reading:** `f.read()`, `f.readline()`, `f.readlines()`, `for line in f:`""",
        "example": 'with open("test_output.txt", "w") as f:\n    f.write("Line 1\\n")\n    f.write("Line 2\\n")\n\nwith open("test_output.txt") as f:\n    for i, line in enumerate(f, 1):\n        print(f"{i}: {line.strip()}")\n\nimport os\nos.remove("test_output.txt")\nprint("Cleaned up.")',
        "exercise": "Write 5 favorite foods to a file, then read and print them with line numbers.",
        "hint": 'foods = ["Pizza", "Sushi", "Tacos", "Pasta", "Curry"]\nwith open("foods.txt", "w") as f:\n    for food in foods:\n        f.write(food + "\\n")\nwith open("foods.txt") as f:\n    for i, line in enumerate(f, 1):\n        print(f"{i}. {line.strip()}")',
        "quiz_q": "What does the `with` statement do for files?",
        "quiz_opts": ["Makes read-only", "Auto-closes the file", "Encrypts it", "Creates backup"],
        "quiz_ans": 1,
        "quiz_exp": "'with' ensures the file is closed when the block exits, even on error.",
    },
    # ===== ADVANCED =====
    {
        "title": "11. Classes & OOP",
        "topic": "Object-Oriented Programming",
        "theory": """```python
class ClassName:
    def __init__(self, params):
        self.attribute = value
    def method(self):
        return something
```

**Key:** `__init__` (constructor), `self` (instance ref), inheritance via `class Child(Parent)`, `super()`, `__str__`""",
        "example": 'class Dog:\n    def __init__(self, name, breed):\n        self.name = name\n        self.breed = breed\n    def bark(self):\n        return f"{self.name} says Woof!"\n    def __str__(self):\n        return f"{self.name} ({self.breed})"\n\nclass Puppy(Dog):\n    def bark(self):\n        return f"{self.name} says Yip!"\n\ndog = Dog("Rex", "Labrador")\npuppy = Puppy("Tiny", "Beagle")\nprint(dog)\nprint(dog.bark())\nprint(puppy.bark())',
        "exercise": "Create a BankAccount class with deposit(), withdraw(), and balance.",
        "hint": 'class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n    def deposit(self, amt):\n        self.balance += amt\n        return self.balance\n    def withdraw(self, amt):\n        if amt > self.balance:\n            print("Insufficient funds")\n            return self.balance\n        self.balance -= amt\n        return self.balance\n\nacc = BankAccount("Alice", 100)\nprint(acc.deposit(50))\nprint(acc.withdraw(200))',
        "quiz_q": "What does 'self' refer to?",
        "quiz_opts": ["The class", "The current instance", "The parent", "Nothing"],
        "quiz_ans": 1,
        "quiz_exp": "'self' is the specific instance the method is called on.",
    },
    {
        "title": "12. Error Handling",
        "topic": "Try / Except / Finally",
        "theory": """```python
try:
    risky code
except SpecificError as e:
    handle it
else:
    runs if no exception
finally:
    always runs
```

Custom: `class MyError(Exception): pass`""",
        "example": 'try:\n    print(10 / 0)\nexcept ZeroDivisionError as e:\n    print(f"Error: {e}")\n\ndef safe_divide(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return "Can\'t divide by zero"\n    finally:\n        print("Attempted")\n\nprint(safe_divide(10, 3))\nprint(safe_divide(10, 0))',
        "exercise": "Write safe_int(value, default=0) that converts to int or returns default.",
        "hint": 'def safe_int(value, default=0):\n    try:\n        return int(value)\n    except (ValueError, TypeError):\n        return default\n\nprint(safe_int("42"))\nprint(safe_int("hello"))',
        "quiz_q": "When does 'finally' run?",
        "quiz_opts": ["Only on error", "Only on success", "Always", "Never"],
        "quiz_ans": 2,
        "quiz_exp": "'finally' always runs — error or not.",
    },
    {
        "title": "13. Comprehensions",
        "topic": "Concise Collection Building",
        "theory": """```python
[expr for x in iter if cond]      # list
{k: v for k, v in items}          # dict
{expr for x in iter}              # set
(expr for x in iter)              # generator
```""",
        "example": 'print([x**2 for x in range(10)])\nprint([x for x in range(20) if x % 2 == 0])\nprint({w: len(w) for w in ["hello", "world"]})\n\nmatrix = [[i*3+j for j in range(3)] for i in range(3)]\nfor row in matrix:\n    print(row)',
        "exercise": "Get numbers 1-50 divisible by 3. Map 1-5 to cubes as a dict.",
        "hint": 'print([x for x in range(1,51) if x%3==0])\nprint({x: x**3 for x in range(1,6)})',
        "quiz_q": "`[x*2 for x in [1,2,3] if x > 1]` produces?",
        "quiz_opts": ["[2,4,6]", "[4,6]", "[2,4]", "[1,4,6]"],
        "quiz_ans": 1,
        "quiz_exp": "Keeps x=2,3 then doubles → [4, 6].",
    },
    {
        "title": "14. Decorators",
        "topic": "Functions that Modify Functions",
        "theory": """```python
@my_decorator
def func(): ...
# same as: func = my_decorator(func)
```

A decorator takes a function, wraps it, returns the wrapper. Uses: timing, logging, caching, auth.""",
        "example": 'import time\nfrom functools import wraps\n\ndef timer(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        print(f"{func.__name__}: {time.time()-start:.4f}s")\n        return result\n    return wrapper\n\n@timer\ndef slow_add(a, b):\n    time.sleep(0.1)\n    return a + b\n\nprint(slow_add(3, 4))',
        "exercise": "Write a 'debug' decorator that prints function name, args, and return value.",
        "hint": 'from functools import wraps\ndef debug(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        print(f"Call {func.__name__}{args}")\n        result = func(*args, **kwargs)\n        print(f"  -> {result!r}")\n        return result\n    return wrapper\n\n@debug\ndef add(a, b): return a + b\nadd(3, 5)',
        "quiz_q": "What does @wraps(func) preserve?",
        "quiz_opts": ["Speed", "Name and docstring", "Thread safety", "Types"],
        "quiz_ans": 1,
        "quiz_exp": "@wraps copies __name__, __doc__ to the wrapper.",
    },
    {
        "title": "15. Generators",
        "topic": "Lazy Evaluation with yield",
        "theory": """```python
def count(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

Generator expr: `(x**2 for x in range(big))`
Memory efficient — values computed on demand. `yield from` delegates to sub-generators.""",
        "example": 'def fibonacci(limit):\n    a, b = 0, 1\n    while a < limit:\n        yield a\n        a, b = b, a + b\n\nfor n in fibonacci(50):\n    print(n, end=" ")\nprint()\n\nimport sys\nprint(f"List: {sys.getsizeof([x**2 for x in range(10000)])} bytes")\nprint(f"Gen:  {sys.getsizeof((x**2 for x in range(10000)))} bytes")',
        "exercise": "Write a generator yielding primes up to a limit.",
        "hint": 'def primes(limit):\n    for n in range(2, limit+1):\n        if all(n%d!=0 for d in range(2, int(n**0.5)+1)):\n            yield n\nprint(list(primes(50)))',
        "quiz_q": "Main advantage of generators?",
        "quiz_opts": ["Faster", "Memory efficient", "Thread safe", "Type safe"],
        "quiz_ans": 1,
        "quiz_exp": "Generators don't store all values in memory.",
    },
    {
        "title": "16. Lambda & Functional",
        "topic": "map, filter, reduce",
        "theory": """`lambda x: x**2` — anonymous function

`map(func, iter)` — apply to each
`filter(func, iter)` — keep if True
`reduce(func, iter)` — accumulate
`sorted(items, key=func)` — custom sort
`functools.lru_cache` — memoization""",
        "example": 'print(list(map(lambda x: x*2, [1,2,3,4,5])))\nprint(list(filter(lambda x: x%2==0, range(20))))\nprint(sorted(["banana","apple","cherry"], key=len))\n\nfrom functools import reduce\nprint(reduce(lambda a,b: a*b, [1,2,3,4,5]))\n\nfrom functools import lru_cache\n\n@lru_cache(maxsize=None)\ndef fib(n):\n    return n if n < 2 else fib(n-1)+fib(n-2)\nprint(fib(30))',
        "exercise": "Get names > 4 chars, uppercased, using map + filter.",
        "hint": 'names = ["Alice","Bob","Charlie","Dan","Eleanor"]\nprint(list(map(str.upper, filter(lambda n: len(n)>4, names))))',
        "quiz_q": "`reduce(lambda a,b: a+b, [1,2,3,4])` returns?",
        "quiz_opts": ["[1,2,3,4]", "10", "4", "24"],
        "quiz_ans": 1,
        "quiz_exp": "((1+2)+3)+4 = 10.",
    },
    {
        "title": "17. Context Managers",
        "topic": "Setup and Cleanup with 'with'",
        "theory": """Class-based: `__enter__()` and `__exit__()`

Function-based (easier):
```python
from contextlib import contextmanager

@contextmanager
def my_ctx():
    # setup
    yield resource
    # cleanup
```""",
        "example": 'import time\nfrom contextlib import contextmanager\n\n@contextmanager\ndef timer(label):\n    start = time.time()\n    yield\n    print(f"{label}: {time.time()-start:.4f}s")\n\nwith timer("Sum"):\n    print(sum(range(1000000)))',
        "exercise": "Write suppress_errors() that catches and prints exceptions.",
        "hint": 'from contextlib import contextmanager\n\n@contextmanager\ndef suppress_errors():\n    try:\n        yield\n    except Exception as e:\n        print(f"Suppressed: {type(e).__name__}: {e}")\n\nwith suppress_errors():\n    print(1/0)\nprint("Still running!")',
        "quiz_q": "Which method runs on exiting 'with'?",
        "quiz_opts": ["__init__", "__enter__", "__exit__", "__del__"],
        "quiz_ans": 2,
        "quiz_exp": "__exit__ handles cleanup.",
    },
    {
        "title": "18. Dataclasses",
        "topic": "Modern Data Containers",
        "theory": """`@dataclass` auto-generates `__init__`, `__repr__`, `__eq__`.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

`frozen=True` → immutable. `field(default_factory=list)` → mutable defaults.""",
        "example": 'from dataclasses import dataclass, field\n\n@dataclass\nclass Student:\n    name: str\n    age: int\n    grades: list = field(default_factory=list)\n    @property\n    def average(self):\n        return sum(self.grades)/len(self.grades) if self.grades else 0\n\ns = Student("Alice", 20, [90, 85, 92])\nprint(s)\nprint(f"Avg: {s.average:.1f}")',
        "exercise": "Create a Product dataclass with total_value property.",
        "hint": 'from dataclasses import dataclass\n\n@dataclass\nclass Product:\n    name: str\n    price: float\n    quantity: int\n    @property\n    def total_value(self):\n        return self.price * self.quantity\n\nprint(Product("Widget", 9.99, 100))',
        "quiz_q": "@dataclass(frozen=True) does what?",
        "quiz_opts": ["Speeds up", "Makes immutable", "Prevents inheritance", "Disables methods"],
        "quiz_ans": 1,
        "quiz_exp": "frozen=True makes instances immutable and hashable.",
    },
    {
        "title": "19. Type Hints",
        "topic": "Static Typing",
        "theory": """```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

`list[int]`, `dict[str, int]`, `Optional[int]`, `Union[int, str]`

Not enforced at runtime — use `mypy` for static checking.""",
        "example": 'from typing import Optional\n\ndef find(uid: int) -> Optional[dict]:\n    users = {1: {"name": "Alice"}}\n    return users.get(uid)\n\nprint(find(1))\nprint(find(99))\n\ndef process(items: list[str], prefix: str = "") -> list[str]:\n    return [f"{prefix}{i}" for i in items]\nprint(process(["a","b"], "item: "))',
        "exercise": "Write a typed stats() returning dict with min, max, sum, avg.",
        "hint": 'def stats(nums: list[float]) -> dict[str, float]:\n    return {"min": min(nums), "max": max(nums),\n            "sum": sum(nums), "avg": sum(nums)/len(nums)}\nprint(stats([10, 20, 30, 40, 50]))',
        "quiz_q": "Are type hints enforced at runtime?",
        "quiz_opts": ["Yes", "No, just docs", "Only strict mode", "Only functions"],
        "quiz_ans": 1,
        "quiz_exp": "Not enforced. Use mypy for static checking.",
    },
    {
        "title": "20. Async / Await",
        "topic": "Asynchronous Programming",
        "theory": """`async def` — coroutine
`await` — pause until ready
`asyncio.run()` — start event loop
`asyncio.gather()` — run concurrently

For: network, file I/O. Not for: CPU-bound work.""",
        "example": 'import asyncio\n\nasync def fetch(name, delay):\n    print(f"Start {name}...")\n    await asyncio.sleep(delay)\n    print(f"Done {name}!")\n    return f"{name} result"\n\nasync def main():\n    results = await asyncio.gather(\n        fetch("X", 0.1), fetch("Y", 0.1), fetch("Z", 0.1))\n    print(f"Results: {results}")\n\nasyncio.run(main())',
        "exercise": "Simulate downloading 3 files concurrently.",
        "hint": 'import asyncio\nasync def dl(name, mb):\n    print(f"Downloading {name}...")\n    await asyncio.sleep(mb*0.01)\n    print(f"Done: {name}")\n    return name\n\nasync def main():\n    files = await asyncio.gather(dl("a.jpg",5), dl("b.mp4",50), dl("c.pdf",2))\n    print(files)\nasyncio.run(main())',
        "quiz_q": "What does 'await' do?",
        "quiz_opts": ["Blocks everything", "Pauses coroutine, lets others run", "Creates thread", "Cancels task"],
        "quiz_ans": 1,
        "quiz_exp": "'await' pauses the coroutine, letting the event loop run others.",
    },
]


# ---------------------------------------------------------------------------
# Safe code execution
# ---------------------------------------------------------------------------
def run_code_safely(code: str) -> tuple[str, str]:
    old_stdout, old_stderr = sys.stdout, sys.stderr
    sys.stdout = captured_out = io.StringIO()
    sys.stderr = captured_err = io.StringIO()
    try:
        exec_globals = {"__builtins__": __builtins__}
        exec(code, exec_globals)
    except Exception:
        traceback.print_exc(file=captured_err)
    finally:
        sys.stdout, sys.stderr = old_stdout, old_stderr
    return captured_out.getvalue(), captured_err.getvalue()


# ---------------------------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------------------------

# Initialize session state
if "completed" not in st.session_state:
    st.session_state.completed = set()
if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = {}

# ---------------------------------------------------------------------------
# Practice Projects Data (defined here so sidebar can reference it)
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "title": "📒 Project 1: Student Grade Manager",
        "description": "A complete student grade management system using classes, file I/O, dictionaries, error handling, and comprehensions.",
        "concepts": "Variables, Strings, Numbers, Lists, Dicts, Conditionals, Loops, Functions, Classes, Error Handling, Comprehensions, File Handling, Type Hints",
        "code": "placeholder",
    },
    {
        "title": "🏦 Project 2: Bank Account System",
        "description": "A banking system with accounts, transactions, interest calculation, and CSV export using OOP, decorators, context managers, and async.",
        "concepts": "Classes, Inheritance, Decorators, Context Managers, Error Handling, Generators, Dataclasses, File I/O, Comprehensions, Type Hints, Lambda",
        "code": "placeholder",
    },
    {
        "title": "📊 Project 3: Data Pipeline & Report Generator",
        "description": "A mini ETL pipeline that loads CSV data, transforms it, generates statistics, and produces a formatted report — using every concept from all 20 lessons.",
        "concepts": "All 20 lessons",
        "code": "placeholder",
    },
]

# Sidebar — mode toggle + navigation
st.sidebar.title("🐍 Learn Python")
st.sidebar.markdown("20 interactive lessons & 3 practice projects")
st.sidebar.divider()

app_mode = st.sidebar.radio("Choose mode:", ["📚 Lessons", "🛠️ Practice Projects"], index=0)

st.sidebar.divider()

if app_mode == "📚 Lessons":
    completed_count = len(st.session_state.completed)
    st.sidebar.progress(completed_count / len(LESSONS), text=f"Progress: {completed_count}/{len(LESSONS)}")

    lesson_titles = []
    for i, lesson in enumerate(LESSONS):
        icon = "✅" if i in st.session_state.completed else "📘" if i < 10 else "🚀"
        lesson_titles.append(f"{icon} {lesson['title']}")

    def _resolve_idx(val):
        """Resolve current lesson index from session state value."""
        if isinstance(val, int):
            return val
        if val in lesson_titles:
            return lesson_titles.index(val)
        # Icon may have changed (📘→✅), match by lesson title text
        for i, t in enumerate(lesson_titles):
            if t[2:] == str(val)[2:]:  # skip icon prefix
                return i
        return 0

    def go_prev():
        current = _resolve_idx(st.session_state.get("lesson_radio", 0))
        if current > 0:
            st.session_state.lesson_radio = lesson_titles[current - 1]

    def go_next():
        current = _resolve_idx(st.session_state.get("lesson_radio", 0))
        if current < len(LESSONS) - 1:
            st.session_state.lesson_radio = lesson_titles[current + 1]

    # Fix stale session value if icon changed
    stored = st.session_state.get("lesson_radio")
    if stored and stored not in lesson_titles:
        idx = _resolve_idx(stored)
        st.session_state.lesson_radio = lesson_titles[idx]

    selected_title = st.sidebar.radio("Select a lesson:", lesson_titles,
                                       key="lesson_radio",
                                       label_visibility="collapsed")
    selected_idx = lesson_titles.index(selected_title) if selected_title in lesson_titles else 0
else:
    selected_idx = 0
    project_choice = st.sidebar.radio(
        "Select a project:",
        [p["title"] for p in PROJECTS],
        label_visibility="collapsed",
    )

st.sidebar.divider()
st.sidebar.caption("Made by [dotnetabhishekai](https://github.com/dotnetabhishekai)")

# Main content
if app_mode == "📚 Lessons":
    lesson = LESSONS[selected_idx]

    st.title(f"{lesson['title']} — {lesson['topic']}")

    tab_theory, tab_code, tab_quiz = st.tabs(["📖 Theory", "💻 Code Editor", "❓ Quiz"])

    with tab_theory:
        st.markdown(lesson["theory"])
        st.divider()
        st.subheader("Example Code")
        st.code(lesson["example"], language="python")
        if st.button("▶️ Run Example", key=f"run_example_{selected_idx}"):
            output, error = run_code_safely(lesson["example"])
            if output:
                st.success("Output:")
                st.code(output, language="text")
            if error:
                st.error("Error:")
                st.code(error, language="text")

    with tab_code:
        st.info(f"**Exercise:** {lesson['exercise']}")
        code = st.text_area("Write your code here:", height=200, key=f"code_editor_{selected_idx}", placeholder="Type your Python code...")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            run_clicked = st.button("▶️ Run Code", key=f"run_code_{selected_idx}", type="primary")
        with col2:
            hint_clicked = st.button("💡 Show Hint", key=f"hint_{selected_idx}")
        with col3:
            if st.button("✅ Mark Complete", key=f"complete_{selected_idx}"):
                st.session_state.completed.add(selected_idx)
                st.rerun()
        if run_clicked and code.strip():
            output, error = run_code_safely(code)
            if output:
                st.success("Output:")
                st.code(output, language="text")
            if error:
                st.error("Error:")
                st.code(error, language="text")
            if not output and not error:
                st.warning("No output produced.")
        if hint_clicked:
            st.markdown("**Hint:**")
            st.code(lesson["hint"], language="python")

    with tab_quiz:
        st.subheader(lesson["quiz_q"])
        answer = st.radio("Choose your answer:", lesson["quiz_opts"], key=f"quiz_radio_{selected_idx}", index=None)
        if st.button("Submit Answer", key=f"quiz_submit_{selected_idx}"):
            if answer is None:
                st.warning("Please select an answer.")
            else:
                selected_opt_idx = lesson["quiz_opts"].index(answer)
                if selected_opt_idx == lesson["quiz_ans"]:
                    st.success(f"✅ Correct! {lesson['quiz_exp']}")
                    st.session_state.quiz_answered[selected_idx] = True
                else:
                    correct = lesson["quiz_opts"][lesson["quiz_ans"]]
                    st.error(f"❌ Not quite. The answer is: **{correct}**\n\n{lesson['quiz_exp']}")
                    st.session_state.quiz_answered[selected_idx] = False

    st.divider()
    col_prev, col_spacer, col_next = st.columns([1, 3, 1])
    with col_prev:
        if selected_idx > 0:
            st.button("← Previous", on_click=go_prev)
    with col_next:
        if selected_idx < len(LESSONS) - 1:
            st.button("Next →", on_click=go_next)

# ---------------------------------------------------------------------------
# Practice Projects — Full Code (updates placeholder entries above)
# ---------------------------------------------------------------------------
_PROJECT_CODES = [
    {
        "title": "📒 Project 1: Student Grade Manager",
        "description": "A complete student grade management system using classes, file I/O, dictionaries, error handling, and comprehensions.",
        "concepts": "Variables, Strings, Numbers, Lists, Dicts, Conditionals, Loops, Functions, Classes, Error Handling, Comprehensions, File Handling, Type Hints",
        "code": '''"""Student Grade Manager — Uses concepts from Lessons 1-19"""
from dataclasses import dataclass, field
from typing import Optional
import json
import os

# --- Data Model (Lesson 11: Classes, Lesson 18: Dataclasses, Lesson 19: Type Hints) ---
@dataclass
class Student:
    name: str
    student_id: str
    grades: dict[str, float] = field(default_factory=dict)

    @property
    def average(self) -> float:
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0.0

    @property
    def letter_grade(self) -> str:
        avg = self.average
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        return "F"

    def __str__(self) -> str:
        return f"{self.name} ({self.student_id}) — Avg: {self.average:.1f} ({self.letter_grade})"


# --- Grade Manager (Lesson 8: Functions, Lesson 12: Error Handling) ---
class GradeManager:
    def __init__(self, filename: str = "grades.json"):
        self.students: dict[str, Student] = {}
        self.filename = filename

    def add_student(self, name: str, student_id: str) -> Student:
        if student_id in self.students:
            raise ValueError(f"Student {student_id} already exists")
        student = Student(name=name, student_id=student_id)
        self.students[student_id] = student
        return student

    def add_grade(self, student_id: str, subject: str, score: float) -> None:
        if student_id not in self.students:
            raise KeyError(f"Student {student_id} not found")
        if not 0 <= score <= 100:
            raise ValueError(f"Score must be 0-100, got {score}")
        self.students[student_id].grades[subject] = score

    # Lesson 15: Generator
    def failing_students(self):
        for s in self.students.values():
            if s.average < 60 and s.grades:
                yield s

    # Lesson 13: Comprehensions
    def class_stats(self) -> dict[str, float]:
        averages = [s.average for s in self.students.values() if s.grades]
        if not averages:
            return {"count": 0, "avg": 0, "highest": 0, "lowest": 0}
        return {
            "count": len(averages),
            "avg": round(sum(averages) / len(averages), 1),
            "highest": round(max(averages), 1),
            "lowest": round(min(averages), 1),
        }

    # Lesson 10: File Handling
    def save(self) -> None:
        data = {sid: {"name": s.name, "grades": s.grades} for sid, s in self.students.items()}
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def load(self) -> None:
        try:
            with open(self.filename) as f:
                data = json.load(f)
            for sid, info in data.items():
                student = Student(name=info["name"], student_id=sid, grades=info["grades"])
                self.students[sid] = student
        except FileNotFoundError:
            pass


# --- Main Program (Lesson 7: Loops, Lesson 6: Conditionals) ---
def main():
    mgr = GradeManager()

    # Add students
    mgr.add_student("Alice Johnson", "S001")
    mgr.add_student("Bob Smith", "S002")
    mgr.add_student("Charlie Brown", "S003")
    mgr.add_student("Diana Lee", "S004")

    # Add grades (Lesson 4: Numbers)
    subjects = {"Math": [92, 78, 55, 88], "Science": [85, 65, 48, 95], "English": [90, 72, 60, 82]}
    student_ids = ["S001", "S002", "S003", "S004"]

    for subject, scores in subjects.items():
        for sid, score in zip(student_ids, scores):
            mgr.add_grade(sid, subject, score)

    # Print all students (Lesson 3: Strings, f-strings)
    print("=== Student Report ===")
    for student in mgr.students.values():
        print(f"  {student}")
        for subj, grade in student.grades.items():
            print(f"    {subj}: {grade}")

    # Class stats
    stats = mgr.class_stats()
    print(f"\\nClass Average: {stats['avg']}, Highest: {stats['highest']}, Lowest: {stats['lowest']}")

    # Failing students (Lesson 15: Generators)
    print("\\nFailing students:")
    for s in mgr.failing_students():
        print(f"  ⚠️ {s.name} — {s.average:.1f}")

    # Top students per subject (Lesson 16: Lambda, Lesson 13: Comprehensions)
    print("\\nTop student per subject:")
    for subject in subjects:
        top = max(mgr.students.values(), key=lambda s: s.grades.get(subject, 0))
        print(f"  {subject}: {top.name} ({top.grades[subject]})")

    # Save (Lesson 10: File I/O)
    mgr.save()
    print(f"\\nSaved to {mgr.filename}")

    # Cleanup
    if os.path.exists(mgr.filename):
        os.remove(mgr.filename)

main()
''',
    },
    {
        "title": "🏦 Project 2: Bank Account System",
        "description": "A banking system with accounts, transactions, interest calculation, and CSV export using OOP, decorators, context managers, and async.",
        "concepts": "Classes, Inheritance, Decorators, Context Managers, Error Handling, Generators, Dataclasses, File I/O, Comprehensions, Type Hints, Lambda",
        "code": '''"""Bank Account System — Uses concepts from Lessons 1-20"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from functools import wraps
from contextlib import contextmanager
import csv
import os

# --- Decorator (Lesson 14) ---
def log_transaction(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print(f"  [LOG] {func.__name__} on {self.account_id}: args={args} → balance={self.balance:.2f}")
        return result
    return wrapper

# --- Data Models (Lesson 18: Dataclasses) ---
@dataclass
class Transaction:
    timestamp: str
    type: str
    amount: float
    balance_after: float
    description: str = ""

@dataclass
class BankAccount:
    owner: str
    account_id: str
    balance: float = 0.0
    account_type: str = "checking"
    transactions: list[Transaction] = field(default_factory=list)

    def _record(self, txn_type: str, amount: float, desc: str = "") -> Transaction:
        txn = Transaction(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            type=txn_type, amount=amount,
            balance_after=self.balance, description=desc
        )
        self.transactions.append(txn)
        return txn

    # Lesson 14: Decorator
    @log_transaction
    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self._record("deposit", amount)
        return self.balance

    @log_transaction
    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds: {self.balance:.2f} available")
        self.balance -= amount
        self._record("withdrawal", amount)
        return self.balance

    # Lesson 15: Generator
    def large_transactions(self, threshold: float = 500):
        for txn in self.transactions:
            if txn.amount >= threshold:
                yield txn

    def __str__(self) -> str:
        return f"[{self.account_id}] {self.owner} — ${self.balance:,.2f} ({self.account_type})"

# --- Savings Account (Lesson 11: Inheritance) ---
class SavingsAccount(BankAccount):
    def __init__(self, owner: str, account_id: str, interest_rate: float = 0.02, **kwargs):
        super().__init__(owner=owner, account_id=account_id, account_type="savings", **kwargs)
        self.interest_rate = interest_rate

    def apply_interest(self) -> float:
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._record("interest", interest, f"Rate: {self.interest_rate:.1%}")
        print(f"  [LOG] Interest ${interest:.2f} applied to {self.account_id}")
        return interest

# --- Context Manager (Lesson 17) ---
@contextmanager
def bank_session(account: BankAccount):
    print(f"\\n--- Session opened for {account.owner} ---")
    starting = account.balance
    try:
        yield account
    except ValueError as e:
        print(f"  ⚠️ Transaction failed: {e}")
    finally:
        diff = account.balance - starting
        sign = "+" if diff >= 0 else ""
        print(f"--- Session closed ({sign}${diff:.2f}) ---")

# --- Export (Lesson 10: File I/O) ---
def export_transactions(account: BankAccount, filename: str) -> None:
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "type", "amount", "balance_after", "description"])
        for txn in account.transactions:
            writer.writerow([txn.timestamp, txn.type, txn.amount, txn.balance_after, txn.description])
    print(f"Exported {len(account.transactions)} transactions to {filename}")

# --- Main (Lesson 7: Loops, Lesson 12: Error Handling) ---
def main():
    checking = BankAccount("Alice", "CHK-001")
    savings = SavingsAccount("Alice", "SAV-001", interest_rate=0.03, balance=1000)

    # Lesson 17: Context manager
    with bank_session(checking):
        checking.deposit(2500)
        checking.deposit(750)
        checking.withdraw(300)
        checking.withdraw(150)

    with bank_session(savings):
        savings.deposit(500)
        savings.apply_interest()

    # Try invalid withdrawal (Lesson 12: Error Handling)
    with bank_session(checking):
        checking.withdraw(99999)

    # Lesson 13: Comprehensions
    all_accounts = [checking, savings]
    total_assets = sum(a.balance for a in all_accounts)
    print(f"\\nTotal assets: ${total_assets:,.2f}")

    # Lesson 15: Generator — large transactions
    print("\\nLarge transactions (>$500):")
    for txn in checking.large_transactions(500):
        print(f"  {txn.type}: ${txn.amount:.2f} on {txn.timestamp}")

    # Lesson 16: Lambda sort
    all_txns = sorted(checking.transactions, key=lambda t: t.amount, reverse=True)
    print(f"\\nLargest transaction: {all_txns[0].type} ${all_txns[0].amount:.2f}")

    # Export
    export_transactions(checking, "checking_txns.csv")
    if os.path.exists("checking_txns.csv"):
        with open("checking_txns.csv") as f:
            print(f.read())
        os.remove("checking_txns.csv")

main()
''',
    },
    {
        "title": "📊 Project 3: Data Pipeline & Report Generator",
        "description": "A mini ETL pipeline that loads CSV data, transforms it, generates statistics, and produces a formatted report — using every concept from all 20 lessons.",
        "concepts": "All 20 lessons: Variables, Strings, Numbers, Lists, Dicts, Conditionals, Loops, Functions, Dicts, File I/O, Classes, Error Handling, Comprehensions, Decorators, Generators, Lambda, Context Managers, Dataclasses, Type Hints, Async",
        "code": '''"""Data Pipeline & Report Generator — Uses ALL 20 lesson concepts"""
import csv
import json
import os
import asyncio
from dataclasses import dataclass, field
from typing import Optional
from functools import wraps, reduce
from contextlib import contextmanager
from datetime import datetime

# === Lesson 14: Decorator — timing ===
def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"  ⏱ {func.__name__}: {time.time()-start:.4f}s")
        return result
    return wrapper

# === Lesson 18: Dataclasses ===
@dataclass
class SalesRecord:
    date: str
    product: str
    category: str
    quantity: int
    price: float
    region: str

    @property
    def revenue(self) -> float:
        return self.quantity * self.price

@dataclass
class ReportStats:
    total_records: int = 0
    total_revenue: float = 0.0
    avg_order_value: float = 0.0
    top_product: str = ""
    top_region: str = ""
    categories: dict = field(default_factory=dict)

# === Lesson 17: Context Manager ===
@contextmanager
def pipeline_stage(name: str):
    print(f"\\n{'='*40}")
    print(f"  Stage: {name}")
    print(f"{'='*40}")
    try:
        yield
    except Exception as e:
        print(f"  ❌ Stage failed: {e}")
        raise
    else:
        print(f"  ✅ {name} complete")

# === Lesson 10: File I/O — Generate sample data ===
def generate_sample_csv(filename: str, n: int = 50) -> str:
    import random
    random.seed(42)
    products = {
        "Laptop": ("Electronics", 899.99), "Phone": ("Electronics", 699.99),
        "Headphones": ("Electronics", 79.99), "Desk": ("Furniture", 249.99),
        "Chair": ("Furniture", 199.99), "Book": ("Education", 29.99),
        "Course": ("Education", 49.99), "Pen Set": ("Stationery", 12.99),
    }
    regions = ["North", "South", "East", "West"]
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "product", "category", "quantity", "price", "region"])
        for i in range(n):
            prod = random.choice(list(products.keys()))
            cat, price = products[prod]
            writer.writerow([
                f"2025-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
                prod, cat, random.randint(1, 20), price, random.choice(regions)
            ])
    return filename

# === Lesson 8: Functions + Lesson 12: Error Handling ===
@timed
def load_data(filename: str) -> list[SalesRecord]:
    records = []
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(SalesRecord(
                    date=row["date"], product=row["product"],
                    category=row["category"],
                    quantity=int(row["quantity"]),
                    price=float(row["price"]),
                    region=row["region"]
                ))
    except FileNotFoundError:
        print("  File not found!")
    except (ValueError, KeyError) as e:
        print(f"  Data error: {e}")
    print(f"  Loaded {len(records)} records")
    return records

# === Lesson 13: Comprehensions + Lesson 16: Lambda ===
@timed
def analyze(records: list[SalesRecord]) -> ReportStats:
    if not records:
        return ReportStats()

    revenues = [r.revenue for r in records]
    total = sum(revenues)

    # Lesson 9: Dictionaries
    product_rev: dict[str, float] = {}
    region_rev: dict[str, float] = {}
    cat_rev: dict[str, float] = {}

    for r in records:
        product_rev[r.product] = product_rev.get(r.product, 0) + r.revenue
        region_rev[r.region] = region_rev.get(r.region, 0) + r.revenue
        cat_rev[r.category] = cat_rev.get(r.category, 0) + r.revenue

    # Lesson 16: Lambda
    top_product = max(product_rev, key=lambda p: product_rev[p])
    top_region = max(region_rev, key=lambda r: region_rev[r])

    # Lesson 16: Reduce
    biggest_order = reduce(lambda a, b: a if a.revenue > b.revenue else b, records)
    print(f"  Biggest single order: {biggest_order.product} ${biggest_order.revenue:.2f}")

    return ReportStats(
        total_records=len(records),
        total_revenue=round(total, 2),
        avg_order_value=round(total / len(records), 2),
        top_product=top_product,
        top_region=top_region,
        categories={k: round(v, 2) for k, v in sorted(cat_rev.items(), key=lambda x: -x[1])},
    )

# === Lesson 15: Generator ===
def high_value_orders(records: list[SalesRecord], threshold: float = 1000):
    for r in records:
        if r.revenue >= threshold:
            yield r

# === Lesson 20: Async ===
async def async_export(stats: ReportStats, filename: str):
    print(f"  Exporting to {filename}...")
    await asyncio.sleep(0.05)  # simulate I/O
    report = f"Sales Report — {datetime.now().strftime(\'%Y-%m-%d\')}\\n"
    report += f"{'='*40}\\n"
    report += f"Total Records: {stats.total_records}\\n"
    report += f"Total Revenue: ${stats.total_revenue:,.2f}\\n"
    report += f"Avg Order Value: ${stats.avg_order_value:,.2f}\\n"
    report += f"Top Product: {stats.top_product}\\n"
    report += f"Top Region: {stats.top_region}\\n\\n"
    report += "Revenue by Category:\\n"
    for cat, rev in stats.categories.items():
        bar = "█" * int(rev / max(stats.categories.values()) * 20)
        report += f"  {cat:15s} ${rev:>10,.2f} {bar}\\n"
    with open(filename, "w") as f:
        f.write(report)
    return report

async def run_exports(stats):
    report = await asyncio.gather(
        async_export(stats, "sales_report.txt"),
    )
    return report[0]

# === Main Pipeline ===
def main():
    csv_file = "sample_sales.csv"

    with pipeline_stage("Generate Data"):
        generate_sample_csv(csv_file, 50)

    with pipeline_stage("Load & Parse"):
        records = load_data(csv_file)

    with pipeline_stage("Analyze"):
        stats = analyze(records)

    with pipeline_stage("High-Value Orders"):
        hv = list(high_value_orders(records, 2000))
        print(f"  Found {len(hv)} orders over $2,000:")
        for r in hv[:5]:
            print(f"    {r.product}: {r.quantity} × ${r.price} = ${r.revenue:,.2f} ({r.region})")

    with pipeline_stage("Export Report"):
        report_text = asyncio.run(run_exports(stats))
        print(report_text)

    # Cleanup
    for f in [csv_file, "sales_report.txt"]:
        if os.path.exists(f):
            os.remove(f)

    print("\\n🎉 Pipeline complete!")

main()
''',
    },
]

# Populate PROJECTS with full code
for i, pc in enumerate(_PROJECT_CODES):
    PROJECTS[i].update(pc)

# (sidebar already handled above)

# Show project if in project mode
if app_mode == "🛠️ Practice Projects":
    project = next(p for p in PROJECTS if p["title"] == project_choice)

    st.components.v1.html(
        """<script>
        setTimeout(() => { window.scrollTo({top: 0, behavior: 'smooth'}); }, 100);
        </script>""",
        height=0,
    )

    st.title(project["title"])
    st.markdown(project["description"])
    st.caption(f"**Concepts used:** {project['concepts']}")

    proj_tab_code, proj_tab_editor, proj_tab_run = st.tabs(["📝 Reference Code", "✏️ Your Code Editor", "▶️ Run Reference"])

    with proj_tab_code:
        st.code(project["code"], language="python")
        if st.button("📋 Copy to Editor", key=f"copy_proj_{project_choice}"):
            st.session_state[f"proj_editor_{project_choice}"] = project["code"]
            st.rerun()

    with proj_tab_editor:
        st.info("Write your own implementation below. Use the reference code tab for guidance.")
        editor_key = f"proj_editor_{project_choice}"
        default_code = st.session_state.get(editor_key, f"# {project['title']}\n# Try writing your own version here!\n\n")
        user_code = st.text_area("Your code:", value=default_code, height=400, key=f"proj_textarea_{project_choice}", placeholder="Write your Python code here...")
        ed_col1, ed_col2, ed_col3 = st.columns([1, 1, 2])
        with ed_col1:
            run_user = st.button("▶️ Run Your Code", key=f"run_user_proj_{project_choice}", type="primary")
        with ed_col2:
            clear_user = st.button("🗑 Clear", key=f"clear_proj_{project_choice}")
        if run_user and user_code.strip():
            output, error = run_code_safely(user_code)
            if output:
                st.success("Output:")
                st.code(output, language="text")
            if error:
                st.error("Error:")
                st.code(error, language="text")
            if not output and not error:
                st.warning("No output produced. Make sure your code calls print() or a main() function.")
        if clear_user:
            st.session_state[editor_key] = ""
            st.rerun()

    with proj_tab_run:
        if st.button("▶️ Run Reference Code", key=f"run_ref_proj_{project_choice}", type="primary"):
            output, error = run_code_safely(project["code"])
            if output:
                st.success("Output:")
                st.code(output, language="text")
            if error:
                st.error("Error:")
                st.code(error, language="text")

# Footer
st.divider()
st.caption("Made by [abhishek]")
