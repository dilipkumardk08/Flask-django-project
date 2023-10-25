create database users;
use users;
create table users (
id int primary key,auto_increment,
name12 varchar(20),
email2 varchar(50),
role12 varchar(20))
insert into users (name12, email12, role12) values
	('dilip' , 'dilip@gmail.com' , 'CEO'),
    ('gowtham' ,  'gowtham@gmail.com' , 'manager'),
    ('purshoh' , 'purshoh@gmail.com' , 'full stack'),
    ('prawin' , 'prawin@gmail.com' , 'software developer'),
    ('nitesh' , 'nitesh@gmail.com' , 'software trainee'),
    ('prawin' , 'prawin@gmail.com' , ' App Developer')
  select * from  users;
select * from users WHERE id = 4;
