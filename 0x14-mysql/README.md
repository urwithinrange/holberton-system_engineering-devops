0x14. MySQL

install mysql-server onto web01 and web02


sudo service mysql start
mysql -u root -p
create USER 'holberton_user'@'localhost' indentified by 'projectcorrection280hbtn'
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost'

### task 2 (web01)
create database tyrell_corp;
use tyrell_corp;
create table nexus6 (id int not null auto_increment, name varchar(256), primary key(id));
insert into nexus6 (name) values ("Leon");
grant select on tyrell_corps.nexus6 to 'holberton_user'@'localhost';

### task 3 (web01)

create user 'replica_user'@'%' identified by 'replica_password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
grant select on mysql.user to 'holberton_user'@'localhost';

### task 4 (web01)
sudo ufw allow 3306
sudo vi /etc/mysql/mysql.conf.d/ mysqld.cnf
+ comment out #bind-address
+ uncomment server id
+ uncomment log_bin
sudo service mysql restart

mysqldump -u root -p tyrell_corp > dump.sql
copy to web-01

#### on web02
sudo vi /etc/mysql/mysql.conf.d/ mysqld.cnf
sudo service mysql restart
create database tyrell_corp
mysql -u root -p tyrell_corp < dump.sql
