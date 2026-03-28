# Learn Python — Interactive Web Tutorial

A browser-based interactive Python tutorial with 20 lessons, a live code editor, quizzes, and progress tracking. Built with Streamlit. No installation needed for end users.

## Live Demo

Deploy your own at [share.streamlit.io](https://share.streamlit.io) — free hosting, accessible to anyone with a browser.

## Features

- 20 structured lessons (10 beginner + 10 advanced)
- Three tabs per lesson: Theory, Code Editor, Quiz
- Live code execution in the browser
- Multiple-choice quizzes with instant feedback
- Progress bar tracking completed lessons
- Dark theme matching the desktop version
- Mobile-friendly responsive layout

## Lessons

### Beginner (1–10)

| # | Topic | Covers |
|---|---|---|
| 1 | Hello World | print(), strings, basic output |
| 2 | Variables | int, float, str, bool, assignment |
| 3 | Strings | f-strings, slicing, methods |
| 4 | Numbers & Math | operators, PEMDAS, type conversion |
| 5 | Lists | indexing, append, sort, comprehensions |
| 6 | Conditionals | if/elif/else, comparison, logical ops |
| 7 | Loops | for, while, range, break, continue, enumerate |
| 8 | Functions | def, return, defaults, *args, **kwargs |
| 9 | Dictionaries | key-value, get, items, comprehensions |
| 10 | File Handling | open, read, write, with statement |

### Advanced (11–20)

| # | Topic | Covers |
|---|---|---|
| 11 | Classes & OOP | __init__, self, inheritance, __str__ |
| 12 | Error Handling | try/except/finally, custom exceptions |
| 13 | Comprehensions | list, dict, set, generator, nested |
| 14 | Decorators | @wraps, decorator factories, timing |
| 15 | Generators | yield, yield from, memory efficiency |
| 16 | Lambda & Functional | map, filter, reduce, lru_cache |
| 17 | Context Managers | __enter__/__exit__, @contextmanager |
| 18 | Dataclasses | @dataclass, frozen, field, @property |
| 19 | Type Hints | Optional, Union, list[int], mypy |
| 20 | Async / Await | asyncio.run, gather, coroutines |

## Run Locally

```bash
cd streamlit_app
pip install streamlit
streamlit run learn_python_web.py
```

Opens at `http://localhost:8501` in your browser.

## Deploy to Streamlit Cloud (Free)

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Learn Python web app"
git remote add origin https://github.com/dotnetabhishekai/learn-python.git
git push -u origin main
```

### Step 2: Deploy

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository
5. Set main file path to `streamlit_app/learn_python_web.py`
6. Click "Deploy"

Your app will be live at a URL like:
```
https://dotnetabhishekai-learn-python.streamlit.app
```

### Step 3: Share

Share the URL with anyone. They can use the tutorial directly in their browser — no Python installation needed.

## Project Structure

```
streamlit_app/
├── learn_python_web.py          # Main Streamlit app
├── requirements.txt             # Dependencies (just streamlit)
├── .streamlit/
│   └── config.toml              # Dark theme configuration
└── README.md                    # This file
```

## How It Works

### Theory Tab
Displays lesson content as formatted Markdown with syntax-highlighted code blocks. Includes a "Run Example" button that executes the example code and shows output.

### Code Editor Tab
A text area where users write Python code. Three buttons:
- **Run Code** — executes the code and displays stdout/stderr
- **Show Hint** — reveals a solution hint
- **Mark Complete** — adds a checkmark in the sidebar

Code runs server-side using `exec()` with captured stdout/stderr. Output and errors are displayed in styled containers.

### Quiz Tab
Multiple-choice questions with radio buttons. On submit, shows whether the answer is correct along with an explanation.

### Progress Tracking
Completed lessons are tracked in Streamlit's session state. The sidebar shows a progress bar and checkmarks next to completed lessons. Progress resets on page refresh (session-based).

## Customization

### Adding a New Lesson

Add a new dict to the `LESSONS` list in `learn_python_web.py`:

```python
{
    "title": "21. New Topic",
    "topic": "Description",
    "theory": "Markdown content...",
    "example": "print('example code')",
    "exercise": "What the user should try.",
    "hint": "print('hint code')",
    "quiz_q": "Question?",
    "quiz_opts": ["A", "B", "C", "D"],
    "quiz_ans": 1,       # 0-indexed
    "quiz_exp": "Explanation of the answer.",
}
```

### Changing the Theme

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#4a4aff"
backgroundColor = "#0f0f1a"
secondaryBackgroundColor = "#12122a"
textColor = "#ccccee"
font = "sans serif"
```

### Persistent Progress

To save progress across sessions, replace `st.session_state` with a database or file-based storage. For single-user local use, you could write to a JSON file similar to the desktop version.

## Desktop Version

The original Tkinter desktop version is available as `learn_python.py` in the parent directory. It has the same 20 lessons with a native desktop UI. Run it with:

```bash
python learn_python.py
```

## Requirements

- Python 3.10+
- streamlit (installed via `pip install streamlit`)

No other dependencies needed.

---

Made by [dotnetabhishekai](https://github.com/dotnetabhishekai)
