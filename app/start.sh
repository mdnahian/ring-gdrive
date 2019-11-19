#!/bin/bash

tmux new-session -d -s ring-gdriv[e
tmux send-keys "python3 /opt/ring/app/monitor/run.py" C-m
read  -n 1 -p "" input