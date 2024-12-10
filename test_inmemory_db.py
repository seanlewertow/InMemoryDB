import unittest
from inmemory_db import InMemoryDB

class TestInMemoryDB(unittest.TestCase):
    def setUp(self):
        self.db = InMemoryDB()

    def test_overwrite_key_in_transaction(self):
        # 10
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.db.put("A", 10)
        self.assertIsNone(self.db.get("A"))
        self.db.commit()
        self.assertEqual(self.db.get("A"), 10)

    def test_get_values_during_transaction(self):
        # None
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.assertIsNone(self.db.get("A"))

    def test_get_values_after_rollback(self):
        # None
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.db.rollback()
        self.assertIsNone(self.db.get("A"))

    def test_no_side_effects_without_transaction(self):
        # None, 10
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.db.rollback()
        self.assertIsNone(self.db.get("A"))
        self.db.begin_transaction()
        self.db.put("B", 10)
        self.db.commit()
        self.assertEqual(self.db.get("B"), 10)

    def test_fig2_example(self):
        # None, Exception, None, 6, Exception, Exception, None
        self.assertIsNone(self.db.get("A"))
        with self.assertRaises(Exception):
            self.db.put("A", 5)
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.assertIsNone(self.db.get("A"))
        self.db.put("A", 6)
        self.db.commit()
        self.assertEqual(self.db.get("A"), 6)
        with self.assertRaises(Exception):
            self.db.commit()
        with self.assertRaises(Exception):
            self.db.rollback()
        self.assertIsNone(self.db.get("B"))
        self.db.begin_transaction()
        self.db.put("B", 10)
        self.db.rollback()
        self.assertIsNone(self.db.get("B"))


if __name__ == "__main__":
    class VerboseTestResult(unittest.TextTestResult):
        def addSuccess(self, test):
            super().addSuccess(test)
            print(f"Success: {test}\n")

    unittest.TextTestRunner(verbosity=2, resultclass=VerboseTestResult).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestInMemoryDB)
    )
