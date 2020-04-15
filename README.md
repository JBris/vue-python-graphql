# vue-python-graphql

## Table of Contents  

* [Quickstart](#quickstart)<a name="quickstart"/>
* [Server](#server)<a name="server"/>
* [Client](#client)<a name="client"/>

## Quickstart

Execute build.sh to create a new .env file. Write your environment-specific details to the .env file and execute build.sh again. 
This will pull all required Docker images and build your containers.

## Server

An asynchronous GraphQL server written in Python. Uses Graphene, Yapsy, and aiohttp. Searches for git repos hosted on GitHub, Bitbucket, and GitLab.  

Visit $PYTHON_HOST/graphiql to access GraphQL Explorer.

See [setup.py](server/setup.py) for dependencies.

## Client

A search app built in Vue, Vuex, Bulma, and Apollo client. Allows users to search for git repos hosted on GitHub, Bitbucket, and GitLab.  

See [package.json](client/package.json) for dependencies.
