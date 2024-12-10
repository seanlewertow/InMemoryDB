class InMemoryDB:
    def __init__(self):
        # committed data
        self.main_store = {}
        # uncommitted data
        self.transaction_store = None

    def get(self, key):
        return self.main_store.get(key)


    def put(self, key, value):
        if self.transaction_store is None:
            raise Exception("No transaction in progress")
        self.transaction_store[key] = value

    def begin_transaction(self):
        if self.transaction_store is not None:
            raise Exception("Transaction already in progress")
        self.transaction_store = {}

    def commit(self):
        if self.transaction_store is None:
            raise Exception("No transaction in progress")
        self.main_store.update(self.transaction_store)
        self.transaction_store = None

    def rollback(self):
        if self.transaction_store is None:
            raise Exception("No transaction in progress")
        self.transaction_store = None
