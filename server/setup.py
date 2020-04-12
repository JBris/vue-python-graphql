import os
import re

from __init__ import app_version

from setuptools import find_packages, setup

install_requires = [
    'psycopg2-binary==2.8.4',
    'aiohttp==3.6.2',
    'aiohttp_cors==0.7.0',
    'gunicorn==19.9.0',
    'graphql-core<3,>=2.1',
    'graphene==2.1.8',
    #Temporary fix until newest aiohttp-graphql commits are available via PyPI
    # 'aiohttp-graphql==1.0.0',
    'yapsy==1.12.2',
    'beautifulsoup4==4.8.2'
]

setup(
    name='vue-aiohttp-graphql',
    version=app_version(),
    description='Async Python web app with GraphQL support.',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)