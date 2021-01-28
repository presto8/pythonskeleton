Introduction
============

pythonskeleton is a basic Python "hello, world" application that
implements many features common to all projects:

- Command-line interface using Click
- Isolated development environment using setuptools/setup.py
- Schemaless data persitence with sqlitedict (which uses pickle for
  serialization)
- Unit testing with pytest
- Simple configuration file support using TOML
- Github workflow for testing each commit

It is intended to be used as a starting point for writing Python-based
command-line applications.


Developer installation
======================

This section will walk you through setting up an isolated development
environment that does not impact the rest of your system.

Requirements:
- Python >= 3.7
- Virtualenv

First, set up virtualenv to isolate the Python modules:

    virtualenv venv   # add --python=$(which python3.7) to force specific python version
    source venv/bin/activate
    pip install --editable .
    source venv/bin/activate

Now try and run the `myapp` executable to make sure everything is working:

    myapp

Finally, create a symbolic link to be able to run myapp even when the virtualenv
is not activated.

    sudo ln -s $PWD/venv/bin/myapp /usr/local/bin/myapp

The virtualenv doesn't really need to be activated again except to run the tests.


Testing
=======

Always activate the virtualenv before starting any tests.  If pytest doesn't
work, try exiting the virtualenv and uninstalling pytest from the system. Then
activate the virtaulenv and pytest should work.

    source venv/bin/activate
    pytest

# `./test`

A convenience shell script called `./test` has been provided. It will
automatically activate the virtualenv if it is not activated, and then run
pytest. If arguments are provided, then any tests in the tests/ directory that
match will be run.

    # test everything
    ./test

    # test only files containing the string "cli"
    ./test cli

If `entr` is installed, use --loop to automatically run the tests whenever any
files change. Open up two windows: run `testloop` in one window and then edit
the source in another. This can be extremely effective for test-driven
development.

    # run tests whenever any source files change
    ./test --loop
