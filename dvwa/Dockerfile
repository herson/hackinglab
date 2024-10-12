# dvwa/Dockerfile

FROM debian:bullseye

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && apt-get install -y \
    apache2 \
    mariadb-server \
    php \
    php-mysqli \
    vim \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Download and install DVWA
RUN wget https://github.com/digininja/DVWA/archive/refs/tags/2.3.zip -O /tmp/dvwa.zip \
    && unzip /tmp/dvwa.zip -d /var/www/html/ \
    && mv /var/www/html/DVWA-2.3 /var/www/html/dvwa \
    && chown -R www-data:www-data /var/www/html/dvwa \
    && chmod -R 755 /var/www/html/dvwa

# Configure Apache
RUN echo "Alias /dvwa /var/www/html/dvwa" > /etc/apache2/conf-available/dvwa.conf \
    && a2enconf dvwa \
    && a2enmod rewrite \
    && service apache2 restart

# Expose necessary ports
EXPOSE 80

# Start Apache in the foreground
CMD ["apachectl", "-D", "FOREGROUND"]