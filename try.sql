create database Itahari_Arts;
use Itahari_Arts;

create table if not exists loyalty(loyalty_level varchar(10) primary key,
 booking_required int, discount varchar(5));
 
 desc loyalty;
 
create table if not exists customer(customer_ref int primary key,
 first_name varchar(20), last_name varchar(20) , address varchar(20), 
 loyalty_level varchar(10), 
 foreign key(loyalty_level) references loyalty(loyalty_level));
 
 desc customer;
 
 create table if not exists customer_contact(customer_ref int primary key, 
contact_number varchar(20) unique,
 email varchar(40) unique,
 foreign key(customer_ref) references customer(customer_ref));
 
 desc customer_contact;
 
create table if not exists payment(payment_id int primary key auto_increment,
 payment_method varchar(20));

desc payment;

create table if not exists event(event_id int primary key, performer varchar(20),
performer_type varchar(20)
);

desc event;

create table if not exists event_detail(detail_id int primary key auto_increment,
event_date date,event_time varchar(10),event_id int,
foreign key(event_id ) references event(event_id)
);

desc event_detail;


create table if not exists venue(venue_id int primary key, venue_name varchar(30), 
address varchar(20), capacity int );

desc venue;

create table if not exists venue_contact(venue_id int primary key ,  
contact_name varchar(20), tel_number varchar(20),
foreign key(venue_id ) references venue(venue_id));

desc venue_contact;

create table if not exists booking(booking_ref int primary key, ticket_qty int,
 booking_date date,full_price varchar(10),customer_ref int, venue_id int, event_id int,
 payment_id int,
 foreign key(event_id ) references event(event_id),
 foreign key(customer_ref) references customer(customer_ref),
 foreign key(venue_id ) references venue(venue_id),
 foreign key(payment_id ) references payment(payment_id));
 
 desc booking;
 
 create table if not exists ticket_collection (collection_id int primary key 
 auto_increment,
collection_type varchar(10));

desc ticket_collection;

create table ticket(ticket_no int primary key, customer_ref int, booking_ref int,
collection_id int,foreign key(customer_ref) references Customer(customer_ref),
foreign key(booking_ref) references booking(booking_ref),
foreign key(collection_id) references ticket_collection(collection_id));

desc ticket;

create table seat(seat_id int primary key auto_increment,seat_row varchar(2),
seat_no int, ticket_no int,
 foreign key(ticket_no) references ticket(ticket_no));
 
 desc seat;
 
 
 insert into loyalty values ('Gold','10','10%'),
 ('Silver','5','7%'),
 ('Bronze','2','5%');
 
 select * from loyalty;
 
 insert into customer values(1,"Manis","Bhattrai","Dharan-4","Gold"),
 (2,"Anmol","Basnet","Itahari-4","Silver"),
 (3,"Biru","Rai","Itahari-2","Gold"),
 (4,"Suv","Regmi","Bir-12","Bronze");
 
 select * from customer;
 
 insert into customer_contact values(1,"07858987789","bmanish@gmail.com"),
 (2,"07754895632","Banmol1@gmail.com"),
 (3,"07587774147","rbiru@gmail.com"),
 (4,"07999852147","dgirl@gmail.com");
 
 select * from customer_contact;
 
 insert into venue values(1,"The Imperial","Itahari-4",450),
(2,"Durbar INN","Itahari-2",200),
(3,"Kundaline","Itahari-1",124),
(4,"Mahjeri","Itahari-12",50);

select * from venue;

insert into venue_contact values(1,"Kiran Rana","07898564456"),
(2,"Pratik Bhusal","07877568854"),
(3,"Achyut Timsina","07785456123"),
(4,"Laxmi Khanal","077875452145");

select * from venue_contact;

insert into event values(1,"The Crew","G5"),
(2,"Sabin Rai","Solo"),
(3,"The Edge","Rock Band");

select * from event;

insert into event_detail(event_date,event_time,event_id)
 values("2019-10-25","7pm",1),
("2019-11-1","7pm",3),
("2019-11-5","2pm",2),
("2019-10-30","7pm",1),
("2019-11-5","2pm",2);

select * from event_detail;

alter table booking ADD full_price varchar(10) after booking_date;

desc booking;

insert into payment(payment_method) 
values("Esewa"),
("Khalti"),
("COD");

select * from payment;

insert into booking values(12,3,"2019-06-12","1200",1,1,1,1),
(25,2,"2019-07-04","1500",2,2,3,3),
(32,2,"2019-09-14","2500",3,3,2,1),
(45,1,"2019-10-04","1200",3,1,1,2),
(47,1,"2019-10-15","2500",4,3,2,3);

select * from booking;

insert into ticket_collection(collection_type) values("Post"),("Collect");

select * from ticket_collection;

desc ticket;

insert into ticket values(1,1,12,1),(2,1,12,1),(3,1,12,1),
(4,1,25,2),(5,2,25,2),(6,3,32,1),
(7,3,32,1),(8,3,45,2),(9,4,47,2);

select * from ticket;

desc seat;

insert into seat(seat_row,seat_no,ticket_no) values("B",34,1),
("B",35,2),("B",36,3),("A",2,4),
("A",3,5),("D",45,6),("D",46,7),
("F",5,8),("H",3,9);

select * from seat;

select count(seat_no),seat_no from seat group by seat_no;
















-- update venue set venue_name="Mahjeri" where venue_id=4;





















truncate table venue;
 
 
 
 
 
 

 
 
 

 
 



 
 




drop table booking;
drop table payment;
drop table event;
-- drop table customer_contact;
drop table event_description;
-- drop table ticket_collection;
drop table venue_contact;
drop table venue;
drop table ticket;
drop table seat;
-- drop table Loyalty;
-- drop table Customer;
-- drop table Loyalty;
-- drop database Itahari_Arts;