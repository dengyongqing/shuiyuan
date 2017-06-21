import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


version = '0.1'

setup(
    name='package_name',
    packages=['package_name'],
    version=version,
    description='small package description',
    long_description=read('README.md'),
    author='al_kricha',
    author_email='krich.al.vl@gmail.com',
    url='https://github.com/gitHubUser/package_name',
    download_url='https://github.com/gitHubUser/package_name/archive{}.tar.gz'.format(version),
    keywords=['key1', 'key2', 'key3'],
    license='MIT',
    classifiers=[ # look here https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
    ],
    install_requires=[
        'selenium'
    ],
)