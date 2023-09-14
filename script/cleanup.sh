#!/bin/bash

# Set the MySQL credentials
username="root"
password="C1sc0123@"
database="mise"

# Remove directories
rm -rf /var/www/html/landscape/configs/authz/*
rm -rf /var/www/html/landscape/configs/ap/*
rm -rf /var/www/html/landscape/configs/authentications/*
rm -rf /var/www/html/landscape/configs/authorizations/*
rm -rf /var/www/html/landscape/configs/authz/*
rm -rf /var/www/html/landscape/configs/conditions/*
rm -rf /var/www/html/landscape/configs/dacl/*
rm -rf /var/www/html/landscape/configs/nad/*
rm -rf /var/www/html/landscape/configs/policyset/*
rm -rf /var/www/html/landscape/configs/sgt/*
rm -rf /root/ise-landscape/mise/configs/authentications/*
rm -rf /root/ise-landscape/mise/configs/authorizations/*
rm -rf /root/ise-landscape/mise/configs/policyset/*
rm -rf /var/www/html/landscape/deployments/*




rm -rf /var/www/html/mise/v0.1/configs/authz/*
rm -rf /var/www/html/mise/v0.1/configs/ap/*
rm -rf /var/www/html/mise/v0.1/configs/authentications/*
rm -rf /var/www/html/mise/v0.1/configs/authorizations/*
rm -rf /var/www/html/mise/v0.1/configs/authz/*
rm -rf /var/www/html/mise/v0.1/configs/conditions/*
rm -rf /var/www/html/mise/v0.1/configs/dacl/*
rm -rf /var/www/html/mise/v0.1/configs/nad/*
rm -rf /var/www/html/mise/v0.1/configs/policyset/*
rm -rf /var/www/html/mise/v0.1/configs/sgt/*
rm -rf /var/www/html/mise/v0.1/configs/condition/*
rm -rf /root/ise-landscape/mise/configs/authentications/*
rm -rf /root/ise-landscape/mise/configs/authorizations/*
rm -rf /root/ise-landscape/mise/configs/policyset/*
rm -rf /var/www/html/mise/v0.1/deployments/*

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
    "DELETE FROM deployhistory;"
    "DELETE FROM policysetdeploy;"
    "DELETE FROM patch;"
    "DELETE FROM cond;"
    "DELETE FROM deploymentcode;"
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
    "ALTER TABLE deployhistory AUTO_INCREMENT = 0;"
    "ALTER TABLE patch AUTO_INCREMENT = 0;"
    "ALTER TABLE policysetdeploy AUTO_INCREMENT = 0;"
    "ALTER TABLE cond AUTO_INCREMENT = 0;"
    "ALTER TABLE deploymentcode AUTO_INCREMENT = 0;"

)

# Run SQL commands
for command in "${sql_commands[@]}"; do
    mysql -u "$username" -p"$password" -D "$database" -e "$command"
done

