from codecs import open
from os import path
from setuptools import find_packages, setup


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='punters_client',
    version='1.0.0b1',
    description='Python client library for www.punters.com.au',
    long_description=long_description,
    keywords='client library punters',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    url='https://github.com/justjasongreen/punters_client',
    author='Jason Green',
    author_email='justjasongreen@gmail.com',
    license='MIT',

    packages=find_packages(exclude=['tests']),
    setup_requires=[],
    install_requires=[
        'cssselect',
        'pytz',
        'tzlocal'
    ],
    extras_require={
        'dev':  [
            'bumpversion',
            'check-manifest'
        ],
        'test': [
            'tox'
        ]
    },
    package_data={
        'punters_client':   []
    },
    data_files=[],
    entry_points={
        'console_scripts':  []
    }
    )
