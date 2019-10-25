#!/bin/sh
python3 start_up.py | xargs -L 1 -P 6 python3 hao_fig4_discount.py
