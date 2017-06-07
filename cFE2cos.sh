#!/bin/bash

# TODO: Replace this with a Makefile instead of a janky script

alias errcho='>&2 printf'

function cFE2cos {
    start_dir=`pwd`

    if [ "$1" == 'init' ]; then
        cd ~/cFE2cos/cFE-6.5.0-OSS-release
        source ./setvars.sh

        cd ~/cFE2cos/cFE-6.5.0-OSS-release/build/cpu1
        make config
        if [ $? -ne 0 ]; then
            errcho 'cFE2cos: Could not "make config" the cFE!\n'
            cd $start_dir
            return 2
        fi

        cd ~/cFE2cos/composite/src
        make config && make init
        if [ $? -ne 0 ]; then
            errcho 'cFE2cos: Could not "make config && make init" composite!\n'
            cd $start_dir
            return 2
        fi

        cd $start_dir
        return 0
    elif [ "$1" == 'build' ]; then
        cd ~/cFE2cos/cFE-6.5.0-OSS-release
        source ./setvars.sh

        cd ~/cFE2cos/build
        if [[ "$2" == '-u' ]]; then
            ./make.py -u
	    echo $?
            return 0
        else
            ./make.py
        fi

        if [ $? -ne 0 ]; then
            errcho 'cFE2cos: make.py failed!\n'
            cd $start_dir
            return 2
        fi

        cd $start_dir
        return 0
    elif [ "$1" == 'run' ]; then
        cd ~/cFE2cos/composite/transfer/
        ./qemu.sh cFE_booter.sh
        cd $start_dir
        return 0
    elif [ "$1" == 'unit-test' ]; then
        cFE2cos build -u
        cFE2cos run
    else
        errcho "Unknown cFE2cos command $1 \nValid options are:\n    init\n    build\n    run\n    unit-test\n"
        cd $start_dir
        return 1
    fi
}

# Setup autocompletion
complete -W 'init build run unit-test' 'cFE2cos'
