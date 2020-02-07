ARG PYTHON_TAG

FROM python:${PYTHON_TAG}

WORKDIR /app
ADD . /app

RUN python setup.py develop

EXPOSE 8080
