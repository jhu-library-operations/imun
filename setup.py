import codecs
import os.path
import re
import sys


from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    # none yet
]

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()

setup_options = dict(
    name = 'imun',
    version = '0.0.1',
    description = 'IMage Update Notifier.',
    long_description = read('README.rst'),
    author = "JHU Libraries Operations Team",
    url = 'https://github.com/jhu-library-operations/imun.git',
    scripts = ['bin/imun'],
    license="Apache License 2.0",
    python_requires=">= 3.6"
    )

setup(**setup_options)
