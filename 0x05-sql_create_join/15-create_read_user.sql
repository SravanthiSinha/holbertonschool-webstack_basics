-- Creating a database and an user with read priviliges
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
