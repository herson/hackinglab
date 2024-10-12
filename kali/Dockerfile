# kali/Dockerfile

FROM kalilinux/kali-rolling

# Replace the default Kali mirror with a reliable one
RUN echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list

# Disable SSL verification temporarily
RUN echo 'Acquire::https::Verify-Peer "false";' > /etc/apt/apt.conf.d/99disable-verification

# Update package lists and install additional tools if needed
RUN apt-get update && apt-get install -y \
    sudo \
    vim \
    git \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Remove the SSL verification override
RUN rm /etc/apt/apt.conf.d/99disable-verification

# Set the default command to bash
CMD ["/bin/bash"]