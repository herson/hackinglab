# zap/Dockerfile

FROM alpine:latest

# Ensure commands run as root
USER root

# Define build argument for ZAP_VERSION
ARG ZAP_VERSION=2.15.0

# Install necessary packages
RUN apk update && apk add --no-cache wget tar

# Download and install ZAP
RUN wget https://github.com/zaproxy/zaproxy/releases/download/v${ZAP_VERSION}/ZAP_${ZAP_VERSION}_Linux.tar.gz -O /tmp/zap.tar.gz \
    && tar -xzf /tmp/zap.tar.gz -C /opt \
    && ln -s /opt/ZAP_${ZAP_VERSION}/zap.sh /usr/local/bin/zap.sh \
    && rm /tmp/zap.tar.gz

# Set the working directory
WORKDIR /opt/ZAP_${ZAP_VERSION}

# Set default command to launch ZAP
CMD ["./zap.sh"]