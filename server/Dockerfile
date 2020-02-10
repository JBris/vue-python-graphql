ARG PYTHON_TAG

FROM python:${PYTHON_TAG}

WORKDIR /app
ADD . /app

RUN python setup.py develop
#Temporary fix until newest aiohttp-graphql commits are available via PyPI
RUN pip install 'aiohttp-graphql @ https://github.com/graphql-python/aiohttp-graphql/archive/24354f2344f39b3c86d8aebcad7437989b569005.tar.gz#egg=aiohttp-graphql-1.0.0'

EXPOSE 8080
