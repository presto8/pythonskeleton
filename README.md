Introduction
============

pythonskeleton is an empty Python development environment including setuptools,
pytest, and Click.


Developer installation
======================

This section will walk you through setting up an isolated development
environment that does not impact the rest of your system.

Requirements:
- Python >= 3.7
- Virtualenv

First, set up virtualenv to isolate the Python modules:

    virtualenv venv
    source venv/bin/activate
    pip install --editable .

Now try and run the `fig` executable to make sure everything is working:

    myapp

Finally, create a symbolic link to be able to run fig even when the virtualenv
is not activated.

    sudo ln -s $PWD/venv/bin/myapp /usr/local/bin/myapp
