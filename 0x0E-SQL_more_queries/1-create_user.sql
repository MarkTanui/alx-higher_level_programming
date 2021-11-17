--  creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 
	'user_0d_1'@'localhost'
	ON *.*
	IDENTIFIED BY 'user_0d_1_pwd'
GRANT ALL TO USER 'user_0d_1'@'localhost';
