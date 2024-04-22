# `packagetest`

This is a sample Python repository that can be executed as a package and imported as a module. Configuring `__init__.py` &amp; `__main__.py`, adjusting `sys.path` and getting the `import`s correct was a chore!

## Sample output
<style>pre strong { color: green; } pre em { color: darkgreen; }  pre span { color: red;}</style>
<pre>
<strong>dcp:packagetest % </strong><em>sh -v test.sh</em>
#!/bin/env sh
  echo ''; cd src; \
python3 foo.py "foo bar"; \
  echo ''; \
python3 packagetest "foo bar"; \
  echo ''; \
python3 -m packagetest "foo bar"; \
  echo ''; cd  ..; \

foo.py: __name__='__main__'
__init__.py: __name__='packagetest'
bar.py: __name__='bar'
foo: packagetest.bar.bar('FOO')
bar: bar.bar('FOO')

__main__.py: __name__='__main__'
__init__.py: __name__='__init__'
bar.py: __name__='bar'
__init__.main(argv): "packagetest 'foo bar'"

__init__.py: __name__='packagetest'
bar.py: __name__='bar'
__main__.py: __name__='__main__'
__init__.py: __name__='__init__'
__init__.main(argv): "<span>...</span>/packagetest/src/packagetest/__main__.py 'foo bar'"

<strong>dcp:packagetest % </strong>

<strong># Within PyCharm...</strong>

<em>./packagetest/.venv/bin/python ./packagetest/src/packagetest</em>
foo.py: __name__='__main__'
__init__.py: __name__='packagetest'
bar.py: __name__='bar'
foo: packagetest.bar.bar('FOO')
bar: bar.bar('FOO')

Process finished with exit code 0

<em>./packagetest/.venv/bin/python ./packagetest/src/packagetest/src/foo.py</em>
__main__.py: __name__='__main__'
__init__.py: __name__='__init__'
bar.py: __name__='bar'
__init__.main(argv): "packagetest<span>.py</span> '-?'"

Process finished with exit code 0</pre>

<hr>

[&#128279; permalink](https://dcpetty.github.io/packagetest) and [&#128297; repository](https://github.com/dcpetty/packagetest) for this page.
