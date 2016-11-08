#!/bin/bash

if [[ -z "$1" ]]; then
    echo "Please provide an archive name from the list below. Please wait."
    tarsnap --list-archives --keyfile ~/.tarsnap/Residency-tarsnap.key
    exit
fi

if [ -e $1/schema.sql ]; then
    echo "Archive already downloaded. Using cached copy."
else
    mkdir $1
    tarsnap -x --keyfile ~/.tarsnap/Residency-tarsnap.key -f $1 -C $1
fi

dropdb Residency_local
createdb Residency_local -O Residency_local
export PGOPTIONS='--client-min-messages=warning'
psql --pset pager=off --quiet -U Residency_local Residency_local < $1/schema.sql
psql --pset pager=off --quiet -U Residency_local Residency_local < $1/data.sql

