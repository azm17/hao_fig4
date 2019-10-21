#!/bin/sh
python3 start_up.py | xargs -L 1 -P 8 python3 hao_fig4.py
