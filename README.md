# [`packagetest`](https://github.com/dcpetty/packagetest)

This is a sample Python repository that can be executed as a package and imported as a module. Configuring `__init__.py` &amp; `__main__.py`, adjusting `sys.path` and getting the `import`s correct was a chore!

This `packagetest` example repository is a means to explore these three possibilities:

1. Importing `packagetest` from another module through `__init__.py` and accessing its contents (including modules) *without* running the `main` function;
1. Importing `packagetest` from the command line through `__main__.py` and running the `main` function;
1. Importing `packagetest` with the `-m` option from the command line through `__init__.py` and running the `main` function.

It has been confusing to make all this work, given the module loading order of `__init__.py` and `__main__.py`, `import`ing using `from` or not, and whether it is even *desirable* to have a module that is both runable and loadable. I was helped by innumerable [StackOverflow](https://stackoverflow.com/) posts, [Python documentation](https://packaging.python.org/), and other [Google](https://google.com/) searches. Here are a few that were invaluable:

| Link | Description |
| --- | --- | 
| [Python Packaging User Guide](https://packaging.python.org/) | '&hellip;a collection of tutorials and references to help you distribute and install Python packages with modern tools.' |
| [Understanding Python imports](https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355) | 'Learn how to import packages and modules (and the difference between the two)' |
| [Relative imports in Python 3 *Explanation*](https://stackoverflow.com/a/28154841/17467335) | 'It amazed me that this question has been around for 9 years, and still popular today with new comments and new answers.' |
| [What are Packages in Python](https://martinxpn.medium.com/what-are-packages-in-python-and-what-is-the-role-of-init-py-files-82-100-days-of-python-325a992b2b13) | '&hellip;and What is the Role of `__init__.py` files?' |
| [The Definitive Guide to Python import Statements](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html) | 'I’ve almost never been able to write correct Python import statements on the first go.' |
| [ImportError](https://iq-inc.com/importerror-attempted-relative-import/) | 'attempted relative import with no known parent package' |
| [My boilerplate](https://stackoverflow.com/a/65780624/17467335) | '&hellip;to make a module with relative imports in a package runnable standalone.' |
| [Realtive imports for the billionth time](https://arc.net/l/quote/zenilyeu) | Even though the question states that the '&hellip;exact replica of the package on pep-0328' gave the *attempted relative import with no known parent package* error, there is a rabbit hole of links. |
| [PEP to change how the main module is delineated](https://mail.python.org/pipermail/python-3000/2007-April/006793.html) | 'The only use case seems to be running scripts that happen to be living inside a module's directory, which I've always seen as an antipattern.' &mdash; [Guido](https://en.wikipedia.org/wiki/Guido_van_Rossum) |
| [importmonkey](https://github.com/hirsimaki-markus/importmonkey) | Look into using `importmonkey` &mdash; I did *not* use it, but it seems simple. |
| [`ultraimport`](https://github.com/ronny-rentner/ultraimport) | Another external library solution (I did *not* use). |

The `packagetest` example repository structure and directory / module layout is as follows:

```text
.
└── packagetest/
 ├── src/
 │ ├── foo.py
 │ └── packagetest/
 │ ├── __init__.py
 │ ├── __main__.py
 │ ├── bar.py
 │ └── baz.py
 ├── .gitignore
 ├── LICENSE
 ├── README.md
 └── test.sh
```

(This [ASCII](https://en.wikipedia.org/wiki/ASCII) folder structure diagram was generated with [tree.nathanfriend.io](tree.nathanfriend.io), '&hellip;an online tree-like utility for generating ASCII folder structure diagrams.')

## Sample output `test1.sh`

The `bash` script `test1.sh` runs commands from the command line to test the three scenarios. Logs labeled with <code>&#x2191;</code> indicate a module's `import`; logs labeled with <code> </code> indicate a function invoked within a modure; logs labeled with <code>&#x2192;</code> indicate a function being called in another module.

<style>.pre strong { color: green; } .pre em { color: darkgreen; } .pre span { color: red;}</style>
<pre class="pre">
<strong>dcp:packagetest % </strong><em>sh test1.sh</em>
# python3 foo.py "foo bar"
INFO: __main__: ↑ foo.py (__package__=None)
INFO:packagetest: ↑ __init__.py (__package__='packagetest')
INFO: bar: ↑ bar.py (__package__='')
INFO: baz: ↑ baz.py (__package__='')
INFO: __init__: ↑ __init__.py (__package__='')
INFO: __main__: foo('FOO')
INFO: __main__: → packagetest.bar.bar('FOO')
INFO: bar: bar.bar('FOO')
INFO: bar: → baz.baz('FOO')
INFO: baz: baz.baz('FOO')
INFO: baz: __init__.__version__='0.0.1'
INFO: __main__: packagetest.__version__='0.0.1'

# python3 packagetest "foo bar"
INFO: __main__: ↑ __main__.py (__package__='')
INFO: __init__: ↑ __init__.py (__package__='')
INFO: bar: ↑ bar.py (__package__='')
INFO: baz: ↑ baz.py (__package__='')
INFO: __init__: main("packagetest 'foo bar'")
INFO: __init__: → bar.bar('MAIN')
INFO: bar: bar.bar('MAIN')
INFO: bar: → baz.baz('MAIN')
INFO: baz: baz.baz('MAIN')
INFO: baz: __init__.__version__='0.0.1'

# python3 -m packagetest "foo bar"
INFO:packagetest: ↑ __init__.py (__package__='packagetest')
INFO: bar: ↑ bar.py (__package__='')
INFO: baz: ↑ baz.py (__package__='')
INFO: __init__: ↑ __init__.py (__package__='')
INFO: __main__: ↑ __main__.py (__package__='packagetest')
INFO: __init__: main("<span>...</span>/packagetest/__main__.py 'foo bar'")
INFO: __init__: → bar.bar('MAIN')
INFO: bar: bar.bar('MAIN')
INFO: bar: → baz.baz('MAIN')
INFO: baz: baz.baz('MAIN')
INFO: baz: __init__.__version__='0.0.1'

<strong>dcp:packagetest % </strong>
</pre>

Using `run` from within [PyCharm](https://www.jetbrains.com/pycharm/) with two different configurations as follows:

<pre class="pre">
<em><span>...</span>/packagetest/.venv/bin/python <span>...</span>/packagetest/src/foo.py</em>
INFO:   __main__: ↑ foo.py (__package__=None)
INFO:packagetest: ↑ __init__.py (__package__='packagetest')
INFO:        bar: ↑ bar.py (__package__='')
INFO:        baz: ↑ baz.py (__package__='')
INFO:   __init__: ↑ __init__.py (__package__='')
INFO:   __main__:   foo('FOO')
INFO:   __main__: → packagetest.bar.bar('FOO')
INFO:        bar:   bar.bar('FOO')
INFO:        bar: → baz.baz('FOO')
INFO:        baz:   baz.baz('FOO')
INFO:        baz:   __init__.__version__='0.0.1'
INFO:   __main__:   packagetest.__version__='0.0.1'

Process finished with exit code 0

<em><span>...</span>/packagetest/.venv/bin/python <span>...</span>/packagetest/src/packagetest</em>
INFO:   __main__: ↑ __main__.py (__package__='')
INFO:   __init__: ↑ __init__.py (__package__='')
INFO:        bar: ↑ bar.py (__package__='')
INFO:        baz: ↑ baz.py (__package__='')
INFO:   __init__:   main("packagetest '-?'")
INFO:   __init__: → bar.bar('MAIN')
INFO:        bar:   bar.bar('MAIN')
INFO:        bar: → baz.baz('MAIN')
INFO:        baz:   baz.baz('MAIN')
INFO:        baz:   __init__.__version__='0.0.1'

Process finished with exit code 0
</pre>

## `alternative`

I was helped by innumerable [StackOverflow](https://stackoverflow.com/) posts, [Python documentation](https://packaging.python.org/), and other [Google](https://google.com/) searches. Here are a few that were invaluable:

| Link | Decription |
| --- | --- |
| https://realpython.com/python-namespace-package/ | RealPython namespace packages. |

The example repository structure and directory / module layout updated with `alternative` is as follows:

```text
.
└── packagetest/
    ├── src/
    │   ├── alternative/
    │   │   ├── _main__.py
    │   │   ├── package/
    │   │   │   ├── a.py
    │   │   │   ├── b.py
    │   │   │   └── c.py
    │   │   └── d.py
    │   ├── packagetest/
    │   │   ├── __init__.py
    │   │   ├── _main__.py
    │   │   ├── bar.py
    │   │   └── baz.py
    │   ├── foo.py
    │   └── qux.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── test1.sh
    └── test2.sh
```

## Sample output `test2.sh`

The `bash` script `test2.sh` runs commands from the command line to test three *other* scenarios.

<pre class="pre">
<strong>dcp:packagetest % </strong><em>sh test2.sh</em>
# python3 qux.py
INFO:            __main__: ↑ qux.py (__package__=None)
INFO:alternative.__main__: ↑ __main__.py (__package__='alternative')
INFO:           package.a: ↑ a.py (__package__='package')
INFO:           package.a:   __main__.__version__='0.0.1'
INFO:           package.b: ↑ b.py (__package__='package')
INFO:           package.c: ↑ c.py (__package__='package')
INFO:alternative.__main__:   a.a='a'
INFO:alternative.__main__:   b.b='b'
INFO:alternative.__main__:   c.c='c'
INFO:                   d: ↑ d.py (__package__='')
INFO:alternative.__main__:   d.d='d'
INFO:            __main__:   dir(alternative.__main__)=['FORMAT', 'OrderedDict', 'Path', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'a', 'b', 'c', 'd', 'logger', 'logging', 'path']
INFO:            __main__:   __main__.a.a='a'
INFO:alternative.package.a: ↑ a.py (__package__='alternative.package')
INFO:alternative.package.a:   __main__.__version__='0.0.1'
INFO:            __main__:   alternative.package.a.a='a'

# python3 alternative
INFO:            __main__: ↑ __main__.py (__package__='')
INFO:           package.a: ↑ a.py (__package__='package')
INFO:alternative.__main__: ↑ __main__.py (__package__='alternative')
INFO:           package.b: ↑ b.py (__package__='package')
INFO:           package.c: ↑ c.py (__package__='package')
INFO:alternative.__main__:   a.a='a'
INFO:alternative.__main__:   b.b='b'
INFO:alternative.__main__:   c.c='c'
INFO:                   d: ↑ d.py (__package__='')
INFO:alternative.__main__:   d.d='d'
INFO:           package.a:   __main__.__version__='0.0.1'
INFO:            __main__:   a.a='a'
INFO:            __main__:   b.b='b'
INFO:            __main__:   c.c='c'
INFO:            __main__:   d.d='d'

# python3 -m alternative
INFO:            __main__: ↑ __main__.py (__package__='alternative')
INFO:           package.a: ↑ a.py (__package__='package')
INFO:alternative.__main__: ↑ __main__.py (__package__='alternative')
INFO:           package.b: ↑ b.py (__package__='package')
INFO:           package.c: ↑ c.py (__package__='package')
INFO:alternative.__main__:   a.a='a'
INFO:alternative.__main__:   b.b='b'
INFO:alternative.__main__:   c.c='c'
INFO:                   d: ↑ d.py (__package__='')
INFO:alternative.__main__:   d.d='d'
INFO:           package.a:   __main__.__version__='0.0.1'
INFO:            __main__:   a.a='a'
INFO:            __main__:   b.b='b'
INFO:            __main__:   c.c='c'
INFO:            __main__:   d.d='d'

<strong>dcp:packagetest % </strong>
</pre>

## TODO

- Finish documentation on how `src/packagetest` works as a runnable and `import`able package / module
- Finish documentation on how `src/alternative` works as a runnable and `import`able package / module

<hr>

[&#128279; permalink](https://dcpetty.github.io/packagetest) and [&#128297; repository](https://github.com/dcpetty/packagetest) for this page.
