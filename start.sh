#!/bin/bash

mkdir -p /tmp/notebook

# Start The SSH Daemon (Server)
/usr/sbin/sshd -D &

# Jupyter Python Notebook Server
python -m notebook \
    --notebook-dir=/tmp/notebook/ \
    --NotebookApp.token='' \
    --NotebookApp.password='' \
    --NotebookApp.port_retries=0 \
    --NotebookApp.allow_origin='*' \
    --NotebookApp.ip='0.0.0.0' \
    --port=54321 \
    --no-browser \
    --allow-root > /proc/1/fd/1 2>&1 &

# FastAPI Server
fastapi dev src/main.py --host 0.0.0.0 --port 80 --reload &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?