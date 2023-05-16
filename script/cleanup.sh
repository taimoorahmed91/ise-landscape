#!/bin/bash

# Set the MySQL credentials
username="root"
password="C1sc0123@"
database="mise"

# Remove directories
rm -rf /var/www/html/landscape/configs/authz/*
rm -rf /var/www/html/landscape/configs/ap/*
rm -rf /var/www/html/landscape/configs/authentications/*
rm -rf /var/www/html/landscape/configs/authz/*
rm -rf /var/www/html/landscape/configs/conditions/*
rm -rf /var/www/html/landscape/configs/dacl/*
rm -rf /var/www/html/landscape/configs/nad/*
rm -rf /var/www/html/landscape/configs/policyset/*
rm -rf /var/www/html/landscape/configs/sgt/*
rm -rf /root/ise-landscape/mise/configs/authentications/*
rm -rf /root/ise-landscape/mise/configs/authorizations/*
rm -rf /root/ise-landscape/mise/configs/authentications/*

# SQL commands
sql_commands=(
    "DELETE FROM ap;"
    "DELETE FROM authentication;"
    "DELETE FROM authorization;"
    "DELETE FROM authz;"
    "DELETE FROM dacl;"
    "DELETE FROM deployments;"
    "DELETE FROM nad;"
    "DELETE FROM policyset;"
    "DELETE FROM sgt;"
    "DELETE FROM uploads;"
    "ALTER TABLE ap AUTO_INCREMENT = 0;"
    "ALTER TABLE authentication AUTO_INCREMENT = 0;"
    "ALTER TABLE authorization AUTO_INCREMENT = 0;"
    "ALTER TABLE authz AUTO_INCREMENT = 0;"
    "ALTER TABLE dacl AUTO_INCREMENT = 0;"
    "ALTER TABLE deployments AUTO_INCREMENT = 0;"
    "ALTER TABLE nad AUTO_INCREMENT = 0;"
    "ALTER TABLE policyset AUTO_INCREMENT = 0;"
    "ALTER TABLE sgt AUTO_INCREMENT = 0;"
    "ALTER TABLE uploads AUTO_INCREMENT = 0;"
)

# Run SQL commands
for command in "${sql_commands[@]}"; do
    mysql -u "$username" -p"$password" -D "$database" -e "$command"
done

