# foo.py
print(f"foo.py: __name__={repr(__name__)}")

import packagetest
def foo(arg):
    """Echo arg."""
    print(f"foo: packagetest.bar.bar({repr(arg)})")
    packagetest.bar.bar(arg)

if __name__ == '__main__':
    foo('FOO')
