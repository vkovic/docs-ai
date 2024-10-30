#!/bin/bash

# Start the SSH daemon
/usr/sbin/sshd -D &

# Start your additional process (replace with your command)
fastapi dev src/main.py --host 0.0.0.0 --port 8081 --reload &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?