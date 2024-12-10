# In-Memory Key-Value Database with Transaction Support

## Description
This project is an **in-memory key-value database** that supports transactions. You can perform the following actions:
- `get(key)` - Retrieve the value of a key.
- `put(key, value)` - Add or update a key-value pair (only during a transaction).
- `begin_transaction()` - Start a transaction.
- `commit()` - Save all changes made in the transaction.
- `rollback()` - Revert all changes made in the transaction.

The database ensures that uncommitted changes are not visible and maintains consistency.

---

## How to Run the Code

### 1. Clone the Repository
Run the following commands in your terminal:
```bash
git clone <your-repo-url>
cd InMemoryDB
```

### 2. Run Test Cases
To test the functionality, run:
```bash
python test_inmemory_db.py
```
You should see the following output:
```plaintext
Ran 5 tests in 0.002s

OK
```

### 3. Run the User Interface
To start the graphical interface, run:
```bash
python inmemory_ui.py
```
Use the buttons and input fields to interact with the database.

### Example Workflow
1. **Start a Transaction**:
   - Click "Begin Transaction".
2. **Put Data**:
   - Enter a key and value, then click "Put".
3. **Commit or Rollback**:
   - Click "Commit" to save changes or "Rollback" to discard them.
4. **Get Data**:
   - Enter a key and click "Get" to retrieve its value.

---

## How This Assignment Can Be Improved

To make this assignment better for future students, here are a few suggestions:

1. **More Detailed Instructions**:
   - Provide more examples in the instructions, such as how transactions handle invalid inputs or what happens when multiple operations fail.

2. **Clearer Requirements**:
   - Clearly state how edge cases (e.g., putting without a transaction) should behave.

3. **Advanced Features**:
   - Allow students to add bonus features, like:
     - Nested transactions.
     - Persistent storage to save the database state.
     - Adding performance tests for handling larger data.

4. **Grading Script**:
   - Include an auto-grading script that checks if the student's database passes all required scenarios. This will simplify grading and ensure consistency.

These changes will make the assignment easier to follow and more engaging for future students.