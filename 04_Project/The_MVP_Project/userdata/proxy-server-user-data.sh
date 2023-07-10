#!/bin/bash
# Install Apache
yum update -y
yum install -y httpd

# Create Apache configuration file
cat > /etc/httpd/conf.d/proxy.conf <<EOL
<VirtualHost *:80>
    ServerName example.com
    ProxyPreserveHost On
    ProxyPass / http://webserver_private_ip/
    ProxyPassReverse / http://webserver_private_ip/
</VirtualHost>
EOL

# Replace webserver_private_ip with the private IP address of your web server
sed -i 's/webserver_private_ip/10.0.0.10/' /etc/httpd/conf.d/proxy.conf

# Start Apache
systemctl start httpd
