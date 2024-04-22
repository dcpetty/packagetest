# __main__.py
print(f"bar.py: __name__={repr(__name__)}")

def bar(arg):
    """Echo arg."""
    print(f"bar: bar.bar({repr(arg)})")
