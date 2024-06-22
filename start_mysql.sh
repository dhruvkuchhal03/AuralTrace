#!/bin/bash

# Define the MySQL root password
MYSQL_ROOT_PASSWORD="Dhruv@2003"

# Start the MySQL server
echo "Starting MySQL server..."
sudo /usr/local/mysql/support-files/mysql.server start

# Log in to MySQL as root
echo "Logging in to MySQL..."
mysql -u root -p"${MYSQL_ROOT_PASSWORD}"
