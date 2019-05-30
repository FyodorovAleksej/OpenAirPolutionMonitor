#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from pip._internal.req import parse_requirements
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [str(ir.req) for ir in parse_requirements('requirements.txt', session='hack')]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Alexey Sergeevich Fyodorov",
    author_email='Fyodorov.aleksej@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Dumper for fetching data from OpenWeatherMap and send to kafka",
    entry_points={
        'console_scripts': [
            'air_pollution_dumper=air_pollution_dumper.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='air_pollution_dumper',
    name='air_pollution_dumper',
    packages=find_packages(include=['air_pollution_dumper']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/FyodorovAleksej/OpenAirPollutionMonitor',
    version='0.1.0',
    zip_safe=False,
)
