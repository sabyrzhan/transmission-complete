#!/usr/bin/env bash
if [ -d $PWD/venv ]; then
    rm -rf $PWD/venv
fi

python3 -m venv ./venv
. ./venv/bin/activate
pip install -r requirements.txt
python move.py
deactivate
