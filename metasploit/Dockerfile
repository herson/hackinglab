# metasploit/Dockerfile

FROM metasploitframework/metasploit-framework:latest

# Ensure commands run as root
USER root

# Update package lists and install packages using apk
RUN apk update && apk add --no-cache vim git

# Copy the entrypoint script
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh

# Make the script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Set the working directory
WORKDIR /home/msf

# Optional: Add custom scripts or configurations
# COPY custom_script.sh /home/msf/

# Set default command to launch msfconsole
CMD ["msfconsole"]