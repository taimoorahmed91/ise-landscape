


#! /bin/bash


mv /root/ise-landscape/script/dump.sql  /root/ise-landscape/script/dump.sql-$(date +%d-%m-%y-%T)
mysqldump --all-databases -u root -pC1sc0123@ > /root/ise-landscape/script/dump.sql
