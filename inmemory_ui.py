import tkinter as tk
from tkinter import messagebox
from inmemory_db import InMemoryDB


class InMemoryDBUI:
    def __init__(self, root):
        self.db = InMemoryDB()
        self.transaction_active = False # transaction state

        # main window
        root.title("In-Memory Key-Value Database")
        root.geometry("600x500")
        root.configure(bg="#1e1e2e")

        # header
        tk.Label(
            root, text="In-Memory Database", font=("Arial", 20, "bold"), bg="#1e1e2e", fg="#f0a500"
        ).pack(pady=10)

        # transaction status display
        self.transaction_label = tk.Label(
            root, text="Transaction: Inactive", font=("Arial", 14), bg="#1e1e2e", fg="#ff5e5e"
        )
        self.transaction_label.pack(pady=5)

        # input frame
        input_frame = tk.Frame(root, bg="#1e1e2e")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Key:", font=("Arial", 12), bg="#1e1e2e", fg="#ffffff").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.key_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.key_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Value:", font=("Arial", 12), bg="#1e1e2e", fg="#ffffff").grid(
            row=1, column=0, padx=10, pady=5
        )
        self.value_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.value_entry.grid(row=1, column=1, padx=10, pady=5)

        # buttons
        buttons_frame = tk.Frame(root, bg="#1e1e2e")
        buttons_frame.pack(pady=10)

        btn_style = {"font": ("Arial", 12), "bg": "#282a36", "fg": "#f8f8f2", "width": 15}

        tk.Button(buttons_frame, text="Get", command=self.get_key, **btn_style).grid(
            row=0, column=0, padx=5, pady=5
        )
        tk.Button(buttons_frame, text="Put", command=self.put_key, **btn_style).grid(
            row=0, column=1, padx=5, pady=5
        )
        tk.Button(buttons_frame, text="Begin Transaction", command=self.begin_transaction, **btn_style).grid(
            row=1, column=0, padx=5, pady=5
        )
        tk.Button(buttons_frame, text="Commit", command=self.commit_transaction, **btn_style).grid(
            row=1, column=1, padx=5, pady=5
        )
        tk.Button(buttons_frame, text="Rollback", command=self.rollback_transaction, **btn_style).grid(
            row=2, column=0, columnspan=2, pady=5
        )

        # logs
        tk.Label(root, text="Log:", font=("Arial", 14, "bold"), bg="#1e1e2e", fg="#f0a500").pack(pady=10)

        self.log_text = tk.Text(root, height=15, width=60, state="disabled", bg="#282a36", fg="#f8f8f2", font=("Arial", 10))
        self.log_text.pack(pady=5)

    def log_message(self, message):
        self.log_text.configure(state="normal")
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.configure(state="disabled")
        self.log_text.see(tk.END)

    def update_transaction_status(self):
        if self.transaction_active:
            self.transaction_label.config(text="Transaction: Active", fg="#5eff5e")
        else:
            self.transaction_label.config(text="Transaction: Inactive", fg="#ff5e5e")

    def get_key(self):
        key = self.key_entry.get()
        if not key:
            messagebox.showerror("Error", "Key field is empty!")
            return
        value = self.db.get(key)
        self.log_message(f"GET {key}: {value}")

    def put_key(self):
        key = self.key_entry.get()
        value = self.value_entry.get()
        if not key or not value:
            messagebox.showerror("Error", "Both key and value fields must be filled!")
            return
        try:
            self.db.put(key, int(value))
            self.log_message(f"PUT {key}: {value}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def begin_transaction(self):
        try:
            self.db.begin_transaction()
            self.transaction_active = True
            self.update_transaction_status()
            self.log_message("Transaction started.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def commit_transaction(self):
        try:
            self.db.commit()
            self.transaction_active = False
            self.update_transaction_status()
            self.log_message("Transaction committed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def rollback_transaction(self):
        try:
            self.db.rollback()
            self.transaction_active = False
            self.update_transaction_status()
            self.log_message("Transaction rolled back.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = InMemoryDBUI(root)
    root.mainloop()
