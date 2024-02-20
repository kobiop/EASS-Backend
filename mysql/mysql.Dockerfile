# Use the official MySQL 5.7 image as the base image
FROM mysql:5.7

# Set the environment variables for MySQL
ENV MYSQL_DATABASE=db
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password
ENV MYSQL_ROOT_PASSWORD=password

# Expose the MySQL port
EXPOSE 3306
