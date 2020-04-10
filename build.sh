#!/usr/bin/env bash

if [ ! -f ".env" ]; then 
    cp .env.example .env 
    echo "Please edit .env before continuing"
    exit 0
fi

if [ ! -f "client/.env" ]; then 
    cp "client/.env.example" "client/.env"
    echo "Creating client/.env..."
fi

while getopts e opt; do
    case $opt in
        e) 
            cp .env.example .env  
            ;;
        *) 
            exit 1
            ;;
  esac
done

. .env

shift $(($OPTIND - 1))

make down
make pull
make dbuild
make up 
