# [`packagetest`](https://github.com/dcpetty/packagetest)

This is a sample Python repository that can be executed as a package and imported as a module. Configuring `__init__.py` &amp; `__main__.py`, adjusting `sys.path` and getting the `import`s correct was a chore!

With a repository structure and directory / module layout as follows, `packagetest` is set up for:

1. Importing `packagetest` from another module through `__init__.py` and accessing its contents (including modules) *without* running the `main` function;
1. Importing `packagetest` from the command line through `__main__.py` and running the `main` function;
1. Importing `packagetest` with the `-m` option from the command line through `__init__.py` and running the `main` function.

```text
.
└── packagetest/
    ├── src/
    │   ├── foo.py
    │   └── packagetest/
    │       ├── __init__.py
    │       ├── __main__.py
    │       ├── bar.py
    │       └── baz.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── test.sh
```

## Sample output

The `bash` script `test.sh` runs commands from the command line as follows:

<style>.pre strong { color: green; } .pre em { color: darkgreen; }  .pre span { color: red;}</style>
<pre class="pre">
<strong>dcp:packagetest % </strong><em>sh test.sh</em>
# python3 foo.py "foo bar"
INFO:   __main__: ↑ foo.py
INFO:packagetest: ↑ __init__.py
INFO:        bar: ↑ bar.py
INFO:        baz: ↑ baz.py
INFO:   __init__: ↑ __init__.py
INFO:   __main__:   foo('FOO')
INFO:   __main__: → packagetest.bar.bar('FOO')
INFO:        bar:   bar.bar('FOO')
INFO:        bar: → baz.baz('FOO')
INFO:        baz:   baz.baz('FOO')
INFO:        baz:   __init__.__version__='0.0.1'
INFO:   __main__:   packagetest.__version__='0.0.1'

# python3 packagetest "foo bar"
INFO:   __main__: ↑ __main__.py
INFO:   __init__: ↑ __init__.py
INFO:        bar: ↑ bar.py
INFO:        baz: ↑ baz.py
INFO:   __init__:   main("packagetest 'foo bar'")
INFO:   __init__: → bar.bar('MAIN')
INFO:        bar:   bar.bar('MAIN')
INFO:        bar: → baz.baz('MAIN')
INFO:        baz:   baz.baz('MAIN')
INFO:        baz:   __init__.__version__='0.0.1'

# python3 -m packagetest "foo bar"
INFO:packagetest: ↑ __init__.py
INFO:        bar: ↑ bar.py
INFO:        baz: ↑ baz.py
INFO:   __init__: ↑ __init__.py
INFO:   __main__: ↑ __main__.py
INFO:   __init__:   main("<span>...</span>/packagetest/__main__.py 'foo bar'")
INFO:   __init__: → bar.bar('MAIN')
INFO:        bar:   bar.bar('MAIN')
INFO:        bar: → baz.baz('MAIN')
INFO:        baz:   baz.baz('MAIN')
INFO:        baz:   __init__.__version__='0.0.1'

<strong>dcp:packagetest % </strong>
</pre>

Using `run` from within [PyCharm](https://www.jetbrains.com/pycharm/) with two different configurations as follows:

<pre class="pre">
<em><span>...</span>/packagetest/.venv/bin/python <span>...</span>/packagetest/src/foo.py</em>
INFO:   __main__: ↑ foo.py
INFO:packagetest: ↑ __init__.py
INFO:        bar: ↑ bar.py
INFO:        baz: ↑ baz.py
INFO:   __init__: ↑ __init__.py
INFO:   __main__:   foo('FOO')
INFO:   __main__: → packagetest.bar.bar('FOO')
INFO:        bar:   bar.bar('FOO')
INFO:        bar: → baz.baz('FOO')
INFO:        baz:   baz.baz('FOO')
INFO:        baz:   __init.__version__='0.0.1'
INFO:   __main__:   packagetest.__version__='0.0.1'

Process finished with exit code 0

<em><span>...</span>/packagetest/.venv/bin/python <span>...</span>/packagetest/src/packagetest</em>
INFO:   __main__: ↑ __main__.py
INFO:   __init__: ↑ __init__.py
INFO:        bar: ↑ bar.py
INFO:        baz: ↑ baz.py
INFO:   __init__:   main("packagetest '-?'")
INFO:   __init__: → bar.bar('MAIN')
INFO:        bar:   bar.bar('MAIN')
INFO:        bar: → baz.baz('MAIN')
INFO:        baz:   baz.baz('MAIN')
INFO:        baz:   __init__.__version__='0.0.1'

Process finished with exit code 0
</pre>

<hr>

[&#128279; permalink](https://dcpetty.github.io/packagetest) and [&#128297; repository](https://github.com/dcpetty/packagetest) for this page.
