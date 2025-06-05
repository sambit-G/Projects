
-- Assignment #1

create table friend (idno numeric(10), fname varchar(24), address varchar(30), age numeric(10), giftvalue numeric(10,2));
INSERT INTO friend VALUES ('01','Ram','Dwarka Sector 10','41','200');
INSERT INTO friend VALUES ('02','Sita','Janakpuri Block C','26','250');
INSERT INTO friend VALUES ('03','Rajesh','Dwarka Sector 15','23','200');
INSERT INTO friend VALUES ('04','Ajit','Noida Sector 11','35','150');
INSERT INTO friend VALUES ('05','Rita','Noida Sector 11','40','200');

select * from friend
select*from friend where age>'40';
select Fname, Age, GiftValue from friend where Age>'35'
select*from friend where Giftvalue>'200'or Age>'20'

-- Assignment #2

create table Employee (Empid numeric(10), Dept char(5), Empname   varchar(15), Address varchar(30), Salary numeric(7));


INSERT INTO Employee VALUES ('101', 'RD01', 'Prince', 'Park Way','15000');
INSERT INTO Employee VALUES ('102','RD01', 'Harry', 'Pebble Street','12000');
INSERT INTO Employee VALUES ('103','RD02', 'Tom', 'Park Avenue','11000');
INSERT INTO Employee VALUES ('104','RD02', 'Susan', 'Model Town','10000');
INSERT INTO Employee VALUES ('105','ED01', 'Mark', 'Victor Crescent','10000');
INSERT INTO Employee VALUES ('106','AD01', 'Francis', 'Chelmsford Park','13000');
INSERT INTO Employee VALUES ('107','GR01', 'Robert', 'Downtown Cross','14000');
INSERT INTO Employee VALUES ('108','RD03', 'Philip', 'Park Avenue','15000');
INSERT INTO Employee VALUES ('109','RD03','Henry', 'Malibu Beach','14000');
INSERT INTO Employee VALUES ('110','AD01','Frank', 'St. Peters Lane','7000');

select * from Employee

Select * from Employee where Dept='RD01'

Select Empname, Dept, Salary from Employee

Select Empname, Dept from Employee where Salary>'13000'

Select * from Employee where Address= 'Park Avenue'

Select Empid, Empname from Employee where Salary='15000' and Address='Park Avenue'

Select Empname from Employee where Dept='RD01'

Select * from Employee where Dept like 'RD%'

Select * from Employee where Dept like 'RD%'

Select min (Salary)  from Employee

Select max (Salary)  from Employee

Select Empname, Dept from Employee where Salary>'12000'

select * from Employee order by Salary

update Employee  set Dept='AD01' where Empname='Susan';

select Empname from Employee where Dept='RD03' and Address='Park Avenue';

select avg (salary) from Employee

select count (salary) from Employee

select * from Employee where salary>'12000'


-- Assignment #3

create table FriendNew (Idno numeric(10)PrimaryKey, Fname varchar(24), Address varchar(30), Age numeric(10), Giftvalue Numeric(10,2));

select*from FriendNew

INSERT INTO FriendNew values('01','Ram','Dwarka Sector 10','41','200');
INSERT INTO FriendNew values('02','Sita','Janakpuri Block c','26', '250.80');
INSERT INTO FriendNew values('03','Rajesh','Dwarka Sector 15','23','200');
INSERT INTO FriendNew values('04','Ajit','Noida Sector 11','35','150.50');
INSERT INTO FriendNew values('05','Rita','Noida Sector 11','40','200');

Select*from FriendNew where Fname like'R%';

Insert into FriendNew values(123,'Anil','Dwarka Sector 11', 23, 29.99);

Update FriendNew Set Age=28 where Fname='Sita';

Delete from FriendNew where Idno=123;

Update FriendNew Set Giftvalue=49.99 where Age=31 OR Age>31;

Alter Table FriendNew Add City Varchar(15);

Update FriendNew Set City='Delhi';

Select Fname, Age from FriendNew 
Order by Fname;

Select Sum (Giftvalue) from FriendNew;

Select Sum(Giftvalue) from FriendNew;

Select Fname, Age from FriendNew where Age = (Select Min(Age) from FriendNew);

Select Count(*) from FriendNew where Age>30;

Select Fname, Giftvalue from Friendnew where Giftvalue = (Select Max(Giftvalue) from FriendNew);

Delete from FriendNew where Idno=123;

Drop Table FriendNew;

