# setup.py
from setuptools import setup

setup(
    name="bma-backend",
    # ... other setup configurations ...
    entry_points={
        "console_scripts": [
            "bma=cli:app",
        ],
    },
)
