-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: medical_data
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `medical_cost_data`
--

DROP TABLE IF EXISTS `medical_cost_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_cost_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bmi` float DEFAULT NULL,
  `diabetes` int DEFAULT NULL,
  `hypertension` int DEFAULT NULL,
  `heart_disease` int DEFAULT NULL,
  `asthma` int DEFAULT NULL,
  `daily_steps` int DEFAULT NULL,
  `sleep_hours` float DEFAULT NULL,
  `stress_level` int DEFAULT NULL,
  `doctor_visits_per_year` int DEFAULT NULL,
  `hospital_admissions` int DEFAULT NULL,
  `medication_count` int DEFAULT NULL,
  `insurance_coverage_pct` int DEFAULT NULL,
  `previous_year_cost` int DEFAULT NULL,
  `annual_medical_cost` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_cost_data`
--

LOCK TABLES `medical_cost_data` WRITE;
/*!40000 ALTER TABLE `medical_cost_data` DISABLE KEYS */;
INSERT INTO `medical_cost_data` VALUES (1,24,1,0,1,0,5934,6,6,5,4,5,85,12569,38680.5),(2,23,0,1,0,1,123443,8,6,7,3,5,5,4,37488.7),(3,24,0,1,0,0,64354,4,9,9,8,5,153,12645,1814.09),(4,22.9,0,0,0,0,7293,10.2,3,2,5,1,68,12645,1313.26),(5,27.5,1,1,1,1,2586,8.3,8,6,3,5,74,4,NULL),(6,24,1,1,1,1,5432,6,0,4,2,7,5,4,NULL);
/*!40000 ALTER TABLE `medical_cost_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-25 12:50:33
