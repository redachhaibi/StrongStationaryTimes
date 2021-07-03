from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='strong_stationary_times',

    version='0.01',

    description='Strong Stationary Times',
    long_description=""" Simulation of strong stationary times (à la Diaconis-Fill) for the Heisenberg group.
    These were described in the paper ""
    """,
    url='',

    author='CHHAIBI Reda',
    author_email='chhaibi.reda@gmail.com',

    license='ApacheV2',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
    ],

    install_requires=["numpy", "matplotlib", "scipy"],

    keywords='',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
