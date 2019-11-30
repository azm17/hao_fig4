#!/bin/sh
python3 start_up_equalizer.py | xargs -L 1 -P 8 python3 wc_equalizer.py
