--  creates the MySQL server user user_0d_1
DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_1'@'%';
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
CREATE USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';
FLUSH PRIVILEGES;
