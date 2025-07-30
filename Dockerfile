FROM ubuntu:24.04

USER root
WORKDIR /root

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y \
    && apt-get upgrade -y   \
    && apt-get dist-upgrade -y \
    && apt-get install -y --no-install-recommends \
        apt-utils \
        build-essential \
        curl \
        iproute2 \
        iputils-ping \
        openvswitch-switch \
        net-tools \
        tcpdump \
        vim \
        x11-xserver-utils \
        xterm   \
        git     \
        sudo \
        python3 \
        python3-pip \
        iperf3 \
        wget \
        mininet \
        openvswitch-testcontroller

# Install additional Python dependencies for Mininet
RUN pip3 install --break-system-packages mininet

# Create symlink for controller
RUN ln -s /usr/bin/ovs-testcontroller /usr/bin/controller

ENV TERM=xterm-color

# Copy demo scripts and topologies
COPY demos/ /root/demos/
COPY script/entrypoint.sh /root/entrypoint.sh
COPY script/test_setup.sh /root/test_setup.sh

# Make scripts executable
RUN chmod +x /root/entrypoint.sh
RUN chmod +x /root/test_setup.sh
RUN chmod +x /root/demos/*.py

# Expose common ports for web servers and other services
EXPOSE 8000 8080 6633 6653

# ENTRYPOINT script
ENTRYPOINT ["/root/entrypoint.sh"]