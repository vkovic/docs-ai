#!/bin/bash

mkdir -p /tmp/notebook

# Start the SSH daemon
#/usr/sbin/sshd -D &

#c.NotebookApp.allow_origin = '*' #allow all origins
#c.NotebookApp.ip = '0.0.0.0' # listen on all IPs
#python -m notebook --notebook-dir=/tmp/pycharm_project_523/ --NotebookApp.port_retries=0 --port=55554 --no-browser &
#python -m notebook --notebook-dir=/tmp/notebook/ --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.port_retries=0 --NotebookApp.allow_origin='*' --NotebookApp.ip='0.0.0.0' --port=54321 --no-browser --allow-root &
#python -m notebook --notebook-dir=/tmp/notebook/ --NotebookApp.token='' --NotebookApp.port_retries=0 --NotebookApp.allow_origin='*' --NotebookApp.ip='0.0.0.0' --port=54321 --no-browser &
#
#
#
#
#notebook --notebook-dir=/app/.notebook/ --no-browser --allow-root

# Jupyter Python Notebook
python -m notebook --notebook-dir=/tmp/notebook/ --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.port_retries=0 --NotebookApp.allow_origin='*' --NotebookApp.ip='0.0.0.0' --port=54321 --no-browser --allow-root > /proc/1/fd/1 2>&1 &

# FastAPI
fastapi dev src/main.py --host 0.0.0.0 --port 80 --reload &

#python -m notebook \
#  --notebook-dir='/tmp/notebook/' \
#  --NotebookApp.token='' \
#  --NotebookApp.password='' \
#  --NotebookApp.port_retries=0 \
#  --NotebookApp.allow_origin='*' \
#  --NotebookApp.ip='0.0.0.0' \
#  --port=54321 \
#  --allow-root \
#  --no-browser \ > /proc/1/fd/1 2>&1 &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?