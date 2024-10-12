# nmap/Dockerfile

FROM instrumentisto/nmap:latest

# Update package lists and install vim using apk
RUN apk update && apk add --no-cache vim

# Set default command to display nmap help
CMD ["nmap", "--help"]