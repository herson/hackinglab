# bwapp/Dockerfile

FROM raesene/bwapp:latest

# Ensure commands run as root
USER root

# Install additional tools or dependencies if necessary
RUN apt-get update && apt-get install -y \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for bWAPP if not already set in docker-compose.yml
ENV UPLOAD_ENABLED=1
ENV MYSQL_DATABASE=bWAPP
ENV MYSQL_USER=bWAPP
ENV MYSQL_PASSWORD=bWAPP
ENV MYSQL_ROOT_PASSWORD=root

# Copy the entrypoint script
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh

# Make the script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Set default command
CMD ["apache2ctl", "-D", "FOREGROUND"]