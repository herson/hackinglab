# wireshark/Dockerfile

FROM jess/wireshark:latest

# Switch to root if necessary
USER root

# Install additional tools
RUN apt-get update && apt-get install -y \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set default command to launch Wireshark
CMD ["wireshark"]