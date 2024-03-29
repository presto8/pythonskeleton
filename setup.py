from setuptools import setup, find_packages
from src.cli import APPNAME

setup(
    name='pythonskeleton',
    version='0.1',
    python_requires='>=3.10',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pytest',
        'sqlitedict',
        'coverage',
        'toml',
    ],
    entry_points=f'''
        [console_scripts]
        {APPNAME}=src.cli:entrypoint
    ''',

    author="Preston Hunt",
    author_email="me@prestonhunt.com",
    description="Python Skeleton",
    keywords="python",
    url="https://github.com/presto8/pythonskeleton",
)
