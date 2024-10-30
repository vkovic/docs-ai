FROM python:3.13-bookworm

# Install OpenSSH server
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

# Set root password
RUN echo 'root:root' | chpasswd

# Allow root login
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Upgrade pip and install setuptools to ensure compatibility
RUN python -m ensurepip --upgrade && \
    python -m pip install --upgrade pip setuptools

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your shell script into the container
COPY start.sh .
RUN chmod +x start.sh

# Set the entrypoint to your script
CMD ["./start.sh"]