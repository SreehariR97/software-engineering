import pytest
import tkinter as tk
from my_app import add_one_item

@pytest.fixture
def app():
    root = tk.Tk()
    return root

def test_add_one_item(app):
    entry = tk.Entry(app)
    listbox = tk.Listbox(app)
    entry.insert(0, "Test Item")
    add_one_item(entry, listbox)
    assert listbox.get(0) == "Test Item"  
