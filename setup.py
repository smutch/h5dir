#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'h5py>=2.6.0',
    'termcolor>=1.1.0',
]

setup(
    name='h5dir',
    version='0.1',
    description="Pretty print a concise listing of an hdf5 file's contents.",
    long_description=readme,
    author="Simon Mutch",
    author_email='smutch.astro@gmail.com',
    url='https://github.com/smutch/h5dir',
    entry_points={
        'console_scripts': [
            'h5dir=h5dir:h5dir'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords=['hdf5', 'h5py', 'h5dir'],
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
