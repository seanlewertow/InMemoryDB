# In-Memory Key-Value Database

This project is a simple in-memory key-value database that supports transactions. It lets you:
- Start a transaction to make multiple changes (`begin_transaction()`).
- Add or update key-value pairs during a transaction (`put(key, value)`).
- Retrieve data at any time (`get(key)`).
- Save your changes with `commit()`.
- Revert changes with `rollback()`.

---

### How to Run

1. **Clone the repository:**
   Open your terminal and run:
   ```bash
   git clone <your-repo-url>
   cd InMemoryDB
   ```
   Make sure you are in the correct directory (`InMemoryDB`) before running the next steps.

2. **Verify Python version:**
   Ensure you have Python 3.7 or higher installed on your system:
   ```bash
   python --version
   ```
   If not installed, download it from [python.org](https://www.python.org/).

3. **Run the test cases:**
   To confirm the functionality of the project:
   ```bash
   python test_inmemory_db.py
   ```
   Expected Output:
   ```plaintext
   Ran 5 tests in 0.002s

   OK
   ```
   If any test fails, check the console for error messages and confirm that you’re in the correct directory.

4. **Launch the graphical interface:**
   Run the following command to start the app:
   ```bash
   python inmemory_ui.py
   ```
   This will open a window where you can interact with the database.

5. **Using the graphical interface:**
   - **Begin Transaction**: Click this button to start a new transaction.
   - **Put**: Enter a key and value, then click "Put" to add or update a key-value pair (must be done during an active transaction).
   - **Commit**: Save all changes made during the transaction.
   - **Rollback**: Revert all changes made in the transaction.
   - **Get**: Enter a key and click "Get" to retrieve its value.

   **Example Workflow**:
   1. Click "Begin Transaction".
   2. Enter a key (`A`) and value (`5`), then click "Put".
   3. Click "Commit" to save the changes.
   4. Enter the key (`A`) in the "Key" field and click "Get" to retrieve the value.

6. **Debugging Common Issues:**
   - If you encounter an error like `ModuleNotFoundError`, ensure all files (`inmemory_db.py`, `inmemory_ui.py`, and `test_inmemory_db.py`) are in the same directory.
   - If the UI does not open, verify that Tkinter is installed (it’s pre-installed with Python on most systems).

---

### Notes for Improvement

If this assignment is reused in the future, some changes can make it better:
1. Add more examples in the instructions to show how the database handles invalid inputs or errors.
2. Introduce advanced features like nested transactions or persistent storage for saving the database state.
3. Provide an automatic grading script that validates test cases without manual intervention.
4. Include expected outputs for test cases and the user interface to ensure graders know what to look for.

These changes would improve the assignment for both students and graders.
