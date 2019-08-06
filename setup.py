#!/usr/bin/env python
from setuptools import setup


setup(
    name='camo-client',
    version='0.2.0',
    author='Ben Olive',
    author_email='sionide21@gmail.com',
    description="A python client for Github's Camo image proxy",
    url='https://github.com/sionide21/camo-client',

    py_modules=['camo'],
    install_requires=['memoize', 'lxml', 'six>=1.12.0'],
    platforms='all',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: Proxy Servers'
    ],
)
