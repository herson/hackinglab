# Use Debian Bullseye as the base image
FROM debian:bullseye

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && apt-get install -y \
    openjdk-11-jre \
    wget \
    unzip \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Download and install WebGoat
RUN wget https://github.com/WebGoat/WebGoat/releases/download/v2023.8/webgoat-2023.8.jar -P /opt/webgoat/

# Expose WebGoat port
EXPOSE 8080

# Define the entrypoint
ENTRYPOINT ["java", "-jar", "/opt/webgoat/WebGoat-2023.8.jar"]