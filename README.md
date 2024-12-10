# In-Memory Key-Value Database

This project is a simple in-memory key-value database that supports transactions. It lets you:
- Start a transaction to make multiple changes (`begin_transaction()`).
- Add or update key-value pairs during a transaction (`put(key, value)`).
- Retrieve data at any time (`get(key)`).
- Save your changes with `commit()`.
- Revert changes with `rollback()`.

### How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repo-url>
   cd InMemoryDB
   ```

2. To check that everything works, run the test cases:
   ```bash
   python test_inmemory_db.py
   ```
   You should see all tests passing.

3. To interact with the database, launch the graphical interface:
   ```bash
   python inmemory_ui.py
   ```
   You’ll see a simple app where you can add, get, or delete data while using transactions.

---

### Notes for Improvement

If this assignment is reused in the future, some small changes would make it better:
1. Add more examples in the instructions to show how the database handles invalid inputs or errors.
2. Allow extra features like nested transactions or persistent storage for saving the database.
3. Include an automatic grading script so test cases can be run directly by graders.

These would make the assignment clearer and easier for both students and graders.