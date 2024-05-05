# [`packagetest`](https://github.com/dcpetty/packagetest)

This is a sample Python repository that can be executed as a package and imported as a module. Configuring `__init__.py` &amp; `__main__.py`, adjusting `sys.path` and getting the `import`s correct was a chore!

This `packagetest` example repository is a means to explore these three possibilities:

1. Importing modules (in `./src/mod` &amp; `./src/tests`) from another module through `__init__.py` and accessing its contents (including submodules) *without* running code in  `__main__.py`;
1. Importing modules (in `./src/mod` &amp; `./src/tests`) from the command line through `__main__.py` and running code in  `__main__.py`;
1. Importing modules (in `./src/mod` &amp; `./src/tests`) with the `-m` option from the command line through `__init__.py` and running code in  `__main__.py`.

It has been confusing to make all this work, given the module loading order of `__init__.py` and `__main__.py`, `import`ing using `from` or not, and whether it is even *desirable* to have a module that is both runable and loadable. I was helped by innumerable [StackOverflow](https://stackoverflow.com/) posts, [Python documentation](https://packaging.python.org/), and other [Google](https://google.com/) searches. Here are a few that were invaluable:

| Link | Description |
| --- | --- | 
| [Python Packaging User Guide](https://packaging.python.org/) | '&hellip;a collection of tutorials and references to help you distribute and install Python packages with modern tools' |
| [What;s a Python Namespace Package](https://realpython.com/python-namespace-package/) | RealPython tutorial on namespace packages |
| [Understanding Python imports](https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355) | 'Learn how to import packages and modules (and the difference between the two)' |
| [Relative imports in Python 3 *Explanation*](https://stackoverflow.com/a/28154841/17467335) | 'It amazed me that this question has been around for 9 years, and still popular today with new comments and new answers' |
| [What are Packages in Python](https://martinxpn.medium.com/what-are-packages-in-python-and-what-is-the-role-of-init-py-files-82-100-days-of-python-325a992b2b13) | '&hellip;and What is the Role of `__init__.py` files?' |
| [The Definitive Guide to Python import Statements](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html) | 'I’ve almost never been able to write correct Python import statements on the first go' |
| [ImportError](https://iq-inc.com/importerror-attempted-relative-import/) | 'attempted relative import with no known parent package' |
| [My boilerplate](https://stackoverflow.com/a/65780624/17467335) | '&hellip;to make a module with relative imports in a package runnable standalone' |
| [For readers in 2023&hellip;](https://stackoverflow.com/a/69099298/17467335) | &hellip;explains relative imports |
| [Realative imports for the billionth time](https://arc.net/l/quote/zenilyeu) | Even though the question states that the '&hellip;exact replica of the package on pep-0328' gave the *attempted relative import with no known parent package* error, there is a rabbit hole of links |
| [PEP to change how the main module is delineated](https://mail.python.org/pipermail/python-3000/2007-April/006793.html) | 'The only use case seems to be running scripts that happen to be living inside a module's directory, which I've always seen as an antipattern.' &mdash; [Guido](https://en.wikipedia.org/wiki/Guido_van_Rossum) |
| [importmonkey](https://github.com/hirsimaki-markus/importmonkey) | Look into using `importmonkey` &mdash; I did *not* use it, but it seems simple |
| [`ultraimport`](https://github.com/ronny-rentner/ultraimport) | Another external library solution (I did *not* use) |

The `packagetest` example repository structure and directory / module layout is as follows:

```text
.
└── packagetest/
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── src/
    │   ├── main.py
    │   ├── mod/
    │   │   ├── __init__.py
    │   │   ├── __main__.py
    │   │   ├── a.py
    │   │   ├── b.py
    │   │   ├── c.py
    │   │   └── pkg/
    │   │       ├── __init__.py
    │   │       └── d.py
    │   ├── run.py
    │   └── tests/
    │       ├── __init__.py
    │       ├── __main__.py
    │       ├── ta.py
    │       ├── tb.py
    │       ├── tc.py
    │       └── td.py
    └── test.sh
```

(This [ASCII](https://en.wikipedia.org/wiki/ASCII) folder structure diagram was generated with [tree.nathanfriend.io](https://arc.net/l/quote/itprgxfi), '&hellip;an online tree-like utility for generating ASCII folder structure diagrams.')

## Sample output `test.sh`

The `bash` script `test.sh` runs commands from the command line to test the three scenarios for the `mod` and `tests` packages in both from the directory containing the module directories and from a parent directory. Logs labeled with <code>&#x2191;</code> indicate a module's `import`; logs labeled with <code> </code> indicate a function invoked within a module; logs labeled with <code>&#x2192;</code> indicate a function being called in another module.

<style>.pre strong { color: green; } .pre em { color: darkgreen; } .pre span { color: red;}</style>
<pre class="pre">
<strong>dcp:packagetest % </strong><em>sh test.sh</em>
# python3 src/main.py "foo bar"
INFO:  __main__: ↑ main.py (__package__=None)
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])

# python3 src/mod "foo bar"
INFO:  __main__: ↑ __main__.py (__package__='')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:  __main__:   dir()=['FORMAT', '_OD', '_P', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg'])
INFO:  __main__:   (pkg.d.d='d')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:  __main__:   dir()=['FORMAT', '_OD', '_P', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'm', 'pkg', 'sys'])
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])
INFO:  __main__:   EXECUTABLE (__version__='0.0.4')

# python3 -m src.mod "foo bar"
INFO:   src.mod: ↑ __init__.py (__package__='src.mod')
INFO: src.mod.a: ↑ a.py (__package__='src.mod')
INFO: src.mod.b: ↑ b.py (__package__='src.mod')
INFO: src.mod.c: ↑ c.py (__package__='src.mod')
INFO: src.mod.b:   b.py (c='c')
INFO: src.mod.a:   a.py (b='b')
INFO:src.mod.pkg: ↑ __init__.py (__package__='src.mod.pkg')
INFO:src.mod.pkg.d: ↑ d.py (__package__='src.mod.pkg')
INFO:src.mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:src.mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:   src.mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:  __main__: ↑ __main__.py (__package__='src.mod')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:  __main__:   dir()=['FORMAT', '_OD', '_P', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg'])
INFO:  __main__:   (pkg.d.d='d')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:  __main__:   dir()=['FORMAT', '_OD', '_P', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'm', 'pkg', 'sys'])
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])
INFO:  __main__:   EXECUTABLE (__version__='0.0.4')

# python3 src/run.py "foo bar"
INFO:  __main__: ↑ run.py (__package__=None)
INFO:     tests: ↑ __init__.py (__package__='tests')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:     tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys'])
INFO:  tests.ta: ↑ ta.py (__package__='tests')
INFO:  tests.tb: ↑ ta.py (__package__='tests')
INFO:  tests.tc: ↑ tc.py (__package__='tests')
INFO:  tests.td: ↑ td.py (__package__='tests')
INFO:     tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys', 'ta', 'tb', 'tc', 'td'])
INFO:tests.__main__: ↑ __main__.py (__package__='tests')
test_a (tests.ta.TestA.test_a) ... INFO:  tests.ta:   test_a()
ok
test_b (tests.tb.TestB.test_b) ... INFO:  tests.tb:   test_b()
ok
test_c (tests.tc.TestC.test_c) ... INFO:  tests.tc:   test_c()
ok
test_d (tests.td.TestD.test_d) ... INFO:  tests.td:   test_d()
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])
ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
test_a (tests.ta.TestA.test_a) ... INFO:  tests.ta:   test_a()
ok
test_b (tests.tb.TestB.test_b) ... INFO:  tests.tb:   test_b()
ok
test_c (tests.tc.TestC.test_c) ... INFO:  tests.tc:   test_c()
ok
test_d (tests.td.TestD.test_d) ... INFO:  tests.td:   test_d()
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])
ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

# python3 src/tests "foo bar"
INFO:  __main__: ↑ __main__.py (__package__='')
INFO:     tests: ↑ __init__.py (__package__='tests')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:     tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys'])
INFO:  tests.ta: ↑ ta.py (__package__='tests')
INFO:  tests.tb: ↑ ta.py (__package__='tests')
INFO:  tests.tc: ↑ tc.py (__package__='tests')
INFO:  tests.td: ↑ td.py (__package__='tests')
INFO:     tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys', 'ta', 'tb', 'tc', 'td'])
test_a (tests.ta.TestA.test_a) ... INFO:  tests.ta:   test_a()
ok
test_b (tests.tb.TestB.test_b) ... INFO:  tests.tb:   test_b()
ok
test_c (tests.tc.TestC.test_c) ... INFO:  tests.tc:   test_c()
ok
test_d (tests.td.TestD.test_d) ... INFO:  tests.td:   test_d()
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])
ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

# python3 -m src.tests "foo bar"
INFO: src.tests: ↑ __init__.py (__package__='src.tests')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO: src.tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys'])
INFO:src.tests.ta: ↑ ta.py (__package__='src.tests')
INFO:src.tests.tb: ↑ ta.py (__package__='src.tests')
INFO:src.tests.tc: ↑ tc.py (__package__='src.tests')
INFO:src.tests.td: ↑ td.py (__package__='src.tests')
INFO: src.tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys', 'ta', 'tb', 'tc', 'td'])
INFO:  __main__: ↑ __main__.py (__package__='src.tests')
INFO:     tests: ↑ __init__.py (__package__='tests')
INFO:     tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys'])
INFO:  tests.ta: ↑ ta.py (__package__='tests')
INFO:  tests.tb: ↑ ta.py (__package__='tests')
INFO:  tests.tc: ↑ tc.py (__package__='tests')
INFO:  tests.td: ↑ td.py (__package__='tests')
INFO:     tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys', 'ta', 'tb', 'tc', 'td'])
test_a (tests.ta.TestA.test_a) ... INFO:  tests.ta:   test_a()
ok
test_b (tests.tb.TestB.test_b) ... INFO:  tests.tb:   test_b()
ok
test_c (tests.tc.TestC.test_c) ... INFO:  tests.tc:   test_c()
ok
test_d (tests.td.TestD.test_d) ... INFO:  tests.td:   test_d()
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])
ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

# python3 foo.py "foo bar"
/Users/dcp/.pyenv/versions/3.12.1/bin/python3: can't open file '/Users/dcp/work/Python/packagetest/src/foo.py': [Errno 2] No such file or directory

# python3 mod "foo bar"
INFO:  __main__: ↑ __main__.py (__package__='')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:  __main__:   dir()=['FORMAT', '_OD', '_P', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg'])
INFO:  __main__:   (pkg.d.d='d')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:  __main__:   dir()=['FORMAT', '_OD', '_P', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'm', 'pkg', 'sys'])
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])
INFO:  __main__:   EXECUTABLE (__version__='0.0.4')

# python3 -m mod "foo bar"
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:  __main__: ↑ __main__.py (__package__='mod')
INFO:  __main__:   dir()=['FORMAT', '_OD', '_P', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg'])
INFO:  __main__:   (pkg.d.d='d')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:  __main__:   dir()=['FORMAT', '_OD', '_P', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'm', 'pkg', 'sys'])
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])
INFO:  __main__:   EXECUTABLE (__version__='0.0.4')

# python3 main.py "foo bar"
INFO:  __main__: ↑ main.py (__package__=None)
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])

# python3 tests "foo bar"
INFO:  __main__: ↑ __main__.py (__package__='')
INFO:     tests: ↑ __init__.py (__package__='tests')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:     tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys'])
INFO:  tests.ta: ↑ ta.py (__package__='tests')
INFO:  tests.tb: ↑ ta.py (__package__='tests')
INFO:  tests.tc: ↑ tc.py (__package__='tests')
INFO:  tests.td: ↑ td.py (__package__='tests')
INFO:     tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys', 'ta', 'tb', 'tc', 'td'])
test_a (tests.ta.TestA.test_a) ... INFO:  tests.ta:   test_a()
ok
test_b (tests.tb.TestB.test_b) ... INFO:  tests.tb:   test_b()
ok
test_c (tests.tc.TestC.test_c) ... INFO:  tests.tc:   test_c()
ok
test_d (tests.td.TestD.test_d) ... INFO:  tests.td:   test_d()
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])
ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

# python3 -m tests "foo bar"
INFO:     tests: ↑ __init__.py (__package__='tests')
INFO:       mod: ↑ __init__.py (__package__='mod')
INFO:     mod.a: ↑ a.py (__package__='mod')
INFO:     mod.b: ↑ b.py (__package__='mod')
INFO:     mod.c: ↑ c.py (__package__='mod')
INFO:     mod.b:   b.py (c='c')
INFO:     mod.a:   a.py (b='b')
INFO:   mod.pkg: ↑ __init__.py (__package__='mod.pkg')
INFO: mod.pkg.d: ↑ d.py (__package__='mod.pkg')
INFO: mod.pkg.d:   dir()=['FORMAT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_logger', '_logging', 'a', 'b', 'c', 'd'])
INFO:   mod.pkg:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_logger', '_logging', 'd'])
INFO:       mod:   dir()=['FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', 'a', 'b', 'c', 'pkg'])
INFO:     tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys'])
INFO:  tests.ta: ↑ ta.py (__package__='tests')
INFO:  tests.tb: ↑ ta.py (__package__='tests')
INFO:  tests.tc: ↑ tc.py (__package__='tests')
INFO:  tests.td: ↑ td.py (__package__='tests')
INFO:     tests:   dir()=['FORMAT', '_OD', '_P', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_logger', '_logging', '_p', 'a', 'b', 'c', 'd', 'pkg', 'sys', 'ta', 'tb', 'tc', 'td'])
INFO:  __main__: ↑ __main__.py (__package__='tests')
test_a (tests.ta.TestA.test_a) ... INFO:  tests.ta:   test_a()
ok
test_b (tests.tb.TestB.test_b) ... INFO:  tests.tb:   test_b()
ok
test_c (tests.tc.TestC.test_c) ... INFO:  tests.tc:   test_c()
ok
test_d (tests.td.TestD.test_d) ... INFO:  tests.td:   test_d()
INFO: mod.pkg.d:   [a.a, b.b, c.c, d, ]=['a', 'b', 'c', 'd'])
ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

<strong>dcp:packagetest % </strong>
</pre>

## TODO

- Finish documentation on how `src/mod` works as a runnable and `import`able package / module
- Finish documentation on how `src/tests` works as a runnable and `import`able package / module

<hr>

[&#128279; permalink](https://dcpetty.github.io/packagetest) and [&#128297; repository](https://github.com/dcpetty/packagetest) for this page.
