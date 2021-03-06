from setuptools import setup, find_packages

setup(
    name='pythonskeleton',
    version='0.1',
    python_requires='>=3.7',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pytest',
        'Click',
        'sqlitedict',
    ],
    entry_points='''
        [console_scripts]
        myapp=myapp.cli:cli
    ''',

    author="Preston Hunt",
    author_email="me@prestonhunt.com",
    description="Python Skeleton",
    keywords="python",
    url="https://github.com/presto8/pythonskeleton",
)
