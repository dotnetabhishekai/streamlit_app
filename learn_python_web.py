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
        exec(code, {"__builtins__": __builtins__}, {})
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

# Sidebar — lesson navigation
st.sidebar.title("🐍 Learn Python")
st.sidebar.markdown("20 interactive lessons")
st.sidebar.divider()

completed_count = len(st.session_state.completed)
st.sidebar.progress(completed_count / len(LESSONS), text=f"Progress: {completed_count}/{len(LESSONS)}")

lesson_titles = []
for i, lesson in enumerate(LESSONS):
    icon = "✅" if i in st.session_state.completed else "📘" if i < 10 else "🚀"
    lesson_titles.append(f"{icon} {lesson['title']}")

selected_idx = st.sidebar.radio("Select a lesson:", range(len(LESSONS)),
                                 format_func=lambda i: lesson_titles[i],
                                 label_visibility="collapsed")

st.sidebar.divider()
st.sidebar.caption("Made by [dotnetabhishekai](https://dotnetabhishek.com)")

# Main content
lesson = LESSONS[selected_idx]

st.title(f"{lesson['title']} — {lesson['topic']}")

# Tabs
tab_theory, tab_code, tab_quiz = st.tabs(["📖 Theory", "💻 Code Editor", "❓ Quiz"])

# Theory tab
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

# Code Editor tab
with tab_code:
    st.info(f"**Exercise:** {lesson['exercise']}")

    code = st.text_area("Write your code here:", height=200,
                        key=f"code_editor_{selected_idx}",
                        placeholder="Type your Python code...")

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

# Quiz tab
with tab_quiz:
    st.subheader(lesson["quiz_q"])

    quiz_key = f"quiz_{selected_idx}"
    answer = st.radio("Choose your answer:", lesson["quiz_opts"],
                       key=f"quiz_radio_{selected_idx}",
                       index=None)

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

# Navigation
st.divider()
col_prev, col_spacer, col_next = st.columns([1, 3, 1])
with col_prev:
    if selected_idx > 0:
        if st.button("← Previous"):
            st.session_state[f"quiz_radio_{selected_idx}"] = None
            st.rerun()
with col_next:
    if selected_idx < len(LESSONS) - 1:
        if st.button("Next →"):
            st.session_state[f"quiz_radio_{selected_idx}"] = None
            st.rerun()

# Footer
st.divider()
st.caption("Made by [dotnetabhishekai](https://github.com/dotnetabhishekai)")
