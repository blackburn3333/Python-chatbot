-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 02, 2020 at 06:12 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `xyz_car_sale`
--

-- --------------------------------------------------------

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
CREATE TABLE IF NOT EXISTS `cars` (
  `car_id` int(11) NOT NULL AUTO_INCREMENT,
  `car_name` varchar(150) NOT NULL,
  `car_brand` varchar(150) NOT NULL,
  `color` varchar(50) NOT NULL,
  `speed` int(3) NOT NULL,
  `price` int(20) NOT NULL,
  PRIMARY KEY (`car_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cars`
--

INSERT INTO `cars` (`car_id`, `car_name`, `car_brand`, `color`, `speed`, `price`) VALUES
(1, 'Toyota corolla', 'Toyota', 'red', 100, 1000),
(2, 'Lamborghini Gallardo', 'Lamborghini', 'black', 240, 125000),
(3, 'Toyota Axio', 'Toyota', 'black', 90, 1500),
(4, 'Maruti Suzuki', 'Maruti', 'green', 60, 900),
(5, 'Honda Swift', 'Honda', 'black', 60, 900);

-- --------------------------------------------------------

--
-- Table structure for table `contact_details`
--

DROP TABLE IF EXISTS `contact_details`;
CREATE TABLE IF NOT EXISTS `contact_details` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_address` varchar(250) NOT NULL,
  `c_number` varchar(50) NOT NULL,
  `c_email` varchar(100) NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact_details`
--

INSERT INTO `contact_details` (`c_id`, `c_address`, `c_number`, `c_email`) VALUES
(1, 'XYZ Colombo 4 address', '0770000001', 'xyz@email.com');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
