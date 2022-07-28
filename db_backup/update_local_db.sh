echo "Updating the DB (Do not forget to stop all connections (KILL LOCAL FLASK SERVER))"
scp -r -i ~/Documents/AWS/physai_web_server_key_pair.pem ubuntu@3.71.5.223:/home/ubuntu/physai-backend/db_scripts/backup.sql .
psql template1 -c 'drop database physai;'
psql template1 -c 'create database physai with owner physai_admin;'
psql -U physai_admin physai < backup.sql
echo "DONE"