# Python Codebook

My Python practice, kept in one place: fundamentals, small projects, and my first steps with DSA, Flask,
Streamlit and SQLite.

| Folder | What's inside |
|---|---|
| `01_python_programs/` | 15 topics: basics, conditionals, loops, lists and dictionaries, functions, error handling, namespaces, tuples and sets, modules and packages, file handling, OOP, advanced Python, logging, multithreading and multiprocessing, memory management |
| `02_DSA/` | pattern programs: diamond, Floyd's triangle, hollow square |
| `03_Flask/` | first Flask apps, Jinja templates, working with an API |
| `04_Streamlit/` | widgets, and an Iris classifier (random forest) |
| `05 SQLite/` | SQLite basics and a sales database, in notebooks |
| `06_Mini_Projects/` | blackjack, coffee machine, guess the number, higher or lower, password generator, rock paper scissors, tip calculator |

## Run something

Most files run on their own:

```bash
python 06_Mini_Projects/guess_the_number.py
```

The Flask and Streamlit folders need a few packages (`pip install flask streamlit pandas scikit-learn`), then
`python 03_Flask/flask_basic01.py` or `streamlit run 04_Streamlit/app.py`.

## Coming next

More DSA (searching, sorting, linked lists, trees), FastAPI, and more SQL.

## License

[MIT](LICENSE)
