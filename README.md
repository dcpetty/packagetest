# `packagetest`

This is a sample Python repository that can be executed as a package and imported as a module. Configuring `__init__.py` &amp; `__main__.py`, adjusting `sys.path` and getting the `import`s correct was a chore!

## Sample output

The `bash` script `test.sh` runs commands from the command line as follows:

<style>pre strong { color: green; } pre em { color: darkgreen; }  pre span { color: red;}</style>
<pre>
<strong>dcp:packagetest % </strong><em>sh test.sh</em>
# python3 foo.py "foo bar"
foo.py: __name__='__main__'
__init__.py: __name__='packagetest'
bar.py: __name__='bar'
foo: packagetest.bar.bar('FOO')
bar: bar.bar('FOO')

# python3 packagetest "foo bar"
__main__.py: __name__='__main__'
__init__.py: __name__='__init__'
bar.py: __name__='bar'
__init__.main(argv): "packagetest 'foo bar'"

# python3 -m packagetest "foo bar"
__init__.py: __name__='packagetest'
bar.py: __name__='bar'
__main__.py: __name__='__main__'
__init__.py: __name__='__init__'
__init__.main(argv): "<span>...</span>/packagetest/src/packagetest/__main__.py 'foo bar'"

<strong>dcp:packagetest % </strong>
</pre>

Using `run` from within [PyCharm](https://www.jetbrains.com/pycharm/) with two different configurations as follows:

<pre>
<em><span>...</span>/packagetest/.venv/bin/python <span>...</span>/packagetest/src/foo.py</em>
foo.py: __name__='__main__'
__init__.py: __name__='packagetest'
bar.py: __name__='bar'
foo: packagetest.bar.bar('FOO')
bar: bar.bar('FOO')

Process finished with exit code 0

<em><span>...</span>/packagetest/.venv/bin/python <span>...</span>/packagetest/src/packagetest</em>
__main__.py: __name__='__main__'
__init__.py: __name__='__init__'
bar.py: __name__='bar'
__init__.main(argv): "packagetest<span>.py</span> '-?'"

Process finished with exit code 0
</pre>

I am not sure why PyCharm adds `'.py'` to `sys.argv[0]` when running a package as a script by its package name.

<hr>

[&#128279; permalink](https://dcpetty.github.io/packagetest) and [&#128297; repository](https://github.com/dcpetty/packagetest) for this page.
