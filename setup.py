from setuptools import setup

readme  = open('README.md').read()

setup(
    name = 'scup-python',
    version = '0.1.0',
    description = 'Unnofficial Python library for the Scup API v1.1. http://www.scup.com/docs/api',
    author = 'Gustavo Machado',
    author_email = 'gdmachado@me.com',
    url = 'https://github.com/gdmachado/scup-python',
    packages = ['scup'],
    install_requires = ['requests >= 0.8', 'six >= 1.6'],
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Operating System :: OS Independent'
    ]
)