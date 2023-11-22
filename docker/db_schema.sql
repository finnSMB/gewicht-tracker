-- -------------------------------------------------------------
-- TablePlus 5.5.2(512)
--
-- https://tableplus.com/
--
-- Database: weight_tracker
-- Generation Time: 2023-11-22 12:32:42.5760
-- -------------------------------------------------------------


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE Database `weight_tracker`;
USE weight_tracker;

CREATE TABLE animal (
    'p_animal_id' int(11) NOT NULL AUTO_INCREMENT,
    'name' VARCHAR(255) NOT NULL,
    'species' VARCHAR(255) NOT NULL,
    'sex' ENUM('male', 'female') NOT NULL,
    'init_weight' FLOAT NOT NULL,
    'birthday' timestamp NULL DEFAULT NULL,
    'created' timestamp NULL DEFAULT current_timestamp(),
    PRIMARY KEY (`p_animal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;;

CREATE TABLE weight (
    'p_weight_id' int(11) NOT NULL AUTO_INCREMENT,
    'f_animal_id' int(11) NOT NULL,
    'created' timestamp NULL DEFAULT current_timestamp(),
    'weight' FLOAT NOT NULL
    PRIMARY KEY (`p_weight_id`),
    KEY `f_animal_id` (`f_animal_id`),
    CONSTRAINT `weight_ibfk_1` FOREIGN KEY (`f_animal_id`) REFERENCES `animal` (`p_animal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;