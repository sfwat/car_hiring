CREATE DATABASE IF NOT EXISTS `car_hiring`;

USE car_hiring;

DROP TABLE IF EXISTS `customers`;

CREATE TABLE `customers` (
	
	`customerId` int PRIMARY KEY AUTO_INCREMENT,
 	`username` varchar(30) NOT NULL,
        `email` varchar(50) UNIQUE,
        `phone` varchar(20) UNIQUE
);

DROP TABLE IF EXISTS `payments`;

CREATE TABLE `payments` (
	
	`paymentId` int PRIMARY KEY AUTO_INCREMENT,
 	`cId` int NOT NULL,
        `payment_details` varchar(50) UNIQUE,
	FOREIGN KEY(`cId`) REFERENCES customers(customerId) ON DELETE CASCADE
);

DROP TABLE IF EXISTS `employees`;

CREATE TABLE `employees` (
	`employeeId` int PRIMARY KEY AUTO_INCREMENT,
	`employee_name` varchar(50) NOT NULL
);


DROP TABLE IF EXISTS `vechiles`;

CREATE TABLE `vechiles` (
	`vechileId` int PRIMARY KEY AUTO_INCREMENT,
	`model` varchar(20) NOT NULL,
	`category` ENUM('small', 'family', 'van') NOT NULL,
	`avalability` BOOLEAN NOT NULL,
	`avalabilty_date` date,
	`employeeId`int NOT NULL,
	FOREIGN KEY(`employeeId`) REFERENCES employees(employeeId) ON DELETE CASCADE
);

DROP TABLE IF EXISTS `inquiries`;

CREATE TABLE `inquiries` (
	`inquiryId` int PRIMARY KEY AUTO_INCREMENT,
	`cId` int NOT NULL,
	`vId` int NOT NULL,
	`employeeId` int NOT NULL,
	FOREIGN KEY(`cId`) REFERENCES customers(customerId) ON DELETE CASCADE,
	FOREIGN KEY(`vId`) REFERENCES vechiles(vechileId) ON DELETE CASCADE,
	FOREIGN KEY(`employeeId`) REFERENCES employees(employeeId) ON DELETE CASCADE
	
);

DROP TABLE IF EXISTS `bookings`;

CREATE TABLE `bookings` (
	`bookingId` int PRIMARY KEY AUTO_INCREMENT,
	`cId` int(10) NOT NULL,
	`vId` int(10) NOT NULL,
	`price` int NOT NULL,
        `start_date` date NOT NULL,
	`end_date` date NOT NULL,
	`paymentId` int not NULL,
	FOREIGN KEY(`cId`) REFERENCES customers(customerId) ON DELETE CASCADE,
	FOREIGN KEY(`vId`) REFERENCES vechiles(vechileId) ON DELETE CASCADE,
	FOREIGN KEY(`paymentId`) REFERENCES payments(paymentId) ON DELETE CASCADE
);

DROP TABLE IF EXISTS `invoices`;

CREATE TABLE `invoices` (
	`invoiceId` int NOT NULL AUTO_INCREMENT,
	`bookingId` int NOT NULL,
	FOREIGN KEY(`bookingId`) REFERENCES bookings(bookingId) ON DELETE CASCADE,
	PRIMARY KEY(`invoiceId`,`bookingId`)

);


DROP TABLE IF EXISTS `confirmation_mails`;

CREATE TABLE `confirmation_mails` (
	`confirmId` int NOT NULL AUTO_INCREMENT,
	`bookingId` int NOT NULL,
	FOREIGN KEY(`bookingId`) REFERENCES bookings(bookingId) ON DELETE CASCADE,
	PRIMARY KEY(`confirmId`,`bookingId`)

);


DELIMITER //

CREATE PROCEDURE DailyReport(
	IN day date
)
BEGIN
	SELECT * 
 	FROM bookings
	WHERE start_date = day;
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER AddBooking
before insert on bookings
for each row
if DATEDIFF(new.end_date, new.start_date) > 7 THEN SET new.end_date = DATE_ADD(new.start_date, INTERVAL 7 DAY);
end if; //

DELIMITER ;


